# coding=utf-8
'''GroupServer-Content View Class
'''
from interfaces import IGSSiteInfo
from zope.component import createObject
from zope.component.interfaces import IFactory
from zope.interface import implements, implementedBy

from App.class_init import InitializeClass

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from Products.XWFCore import XWFUtils

import Products.GSContent.interfaces

class GSSiteInfoFactory(object):
    implements(IFactory)
    
    title = u'GroupServer Site Info Factory'
    descripton = u'Create a new GroupServer site information instance'
    
    def __call__(self, context):
        retval = GSSiteInfo(context)
        return retval
        
    def getInterfaces(self):
        retval = implementedBy(GSSiteInfo)
        assert retval
        return retval

class GSSiteInfo:
    """An implementation of the GroupServer Site Information Interface
    
    This adaptor provides information about the site, based on the context
    of the object.
    """
    implements( IGSSiteInfo )
    def __init__(self, context):
        """Create an GSSiteInfo instance.
        
        ARGUMENTS
            "context" The context of the page.
        
        SIDE EFFECTS
            Sets 
              * "self.context" to the context argument, 
              * "self.siteObj" to the site-instance, and 
              * "self.config" to the site-configuration instance.
        """
        self.context = context
        self.siteObj = self.__get_site_object()
        self.config = self.__get_site_config()
        
    def __get_site_object(self):
        """Get the site-object, which contains the current instance.
        
        This method preforms a search for the site instance among the 
        ancestors of the current object, walking back up the tree looking
        for the object that has the "is_division" property set to "True".
        
        ARGUMENTS
            None.
            
        RETURNS
            The site object.

        SIDE EFFECTS
            None.
            
        ENVIRONMENT
            "self.context": The context of the object.     
        """
        retval = self.context
        markerAttr = 'is_division'
        while retval:
            try:
                if getattr(retval.aq_inner.aq_explicit, markerAttr, False):
                    break
                else:
                    retval = retval.aq_parent
            except:
                break

        try:
            retval = retval.aq_inner.aq_explicit
        except AttributeError:
            retval = None
        return retval
                
    def __get_site_config(self):
        """ Get the site configuration instance from the site object.
        
        ARGUMENTS
            None.
        
        RETURNS
            The site configuration instance.
            
        SIDE EFFECTS
            None.
            
        ENVIRONMENT
            "self.siteObject": The site object.

        """
        if self.siteObj:
            retval = getattr(self.siteObj, 'DivisionConfiguration', None)
        else:
            retval = getattr(self.context, 'GlobalConfiguration', None)
        
        return retval

    @property
    def id(self):
        return self.get_id()
    def get_id(self):
        retval = None
        if self.siteObj:
            retval = self.siteObj.getId()
        return retval
    
    @property
    def name(self):
        return self.get_name()        
    def get_name(self):
        retval = self.config.getProperty('siteName', '')
        if not retval and self.siteObj:
            retval = self.siteObj.title_or_id()
        return retval

    @property
    def title(self):
        retval = self.config.getProperty('siteTitle', self.name)
        if isinstance(retval, str):
            retval = unicode(retval, 'utf-8', 'ignore')
        return retval
        
    @property
    def url(self):
        return self.get_url()        
    def get_url(self):
        '''Gets the URL from the site. It is made up of the canonical 
        host and the canonical port. If the canonical port is not set,
        or is set to port 80, then it is not included in the URL.'''
        retval = '/'

        canonicalHost = self.config.getProperty('canonicalHost', '')
        if canonicalHost:
            retval = 'http://%s' % canonicalHost
        elif self.siteObj:
            retval = '/%s' % self.siteObj.absolute_url(1)

        canonicalPort = self.config.getProperty('canonicalPort', '80')
        if canonicalPort != '80':
          retval = '%s:%s' % (retval, canonicalPort)
          
        return retval
        
    @property
    def showImage(self):
        return self.config.getProperty('showImage', False)

    @property
    def skin(self):
        return self.config.getProperty('skin', 'green')

    def get_path(self):
        retval = '/'.join(self.siteObj.getPhysicalPath())
        assert len(retval) >= 1
        return retval
        
    def get_support_email(self):
        retval = XWFUtils.get_support_email(self.context, self.get_id())
        assert type(retval) == str
        assert retval
        assert '@' in retval
        return retval
        
    def get_property(self, prop, default=None):
        assert self.siteObj, 'Site instance does not exist\n'\
          'Context %s\nID %s' % (self.context, self.id)
        retval = self.siteObj.getProperty(prop, default)
        if isinstance(retval, str):
            retval = unicode(retval, 'utf-8', 'ignore')
        
        return retval
        
class GSSiteHomepageView(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.siteInfo = createObject('groupserver.SiteInfo', context.aq_self)
        self.groupsInfo = createObject('groupserver.GroupsInfo', context.aq_self)

class GSContentView(BrowserView):
    '''View object for standard GroupServer content objects'''
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.__siteInfo = self.__groupsInfo = None
    
    @property
    def siteInfo(self):
        if self.__siteInfo == None:
            self.__siteInfo = createObject('groupserver.SiteInfo', 
                                self.context.aq_self)
        assert self.__siteInfo
        return self.__siteInfo
        
    @property
    def groupsInfo(self):
        if self.__groupsInfo == None:
            self.__groupsInfo = createObject('groupserver.GroupsInfo', 
                                    self.context.aq_self)
        assert self.__groupsInfo
        return self.__groupsInfo
        
    def process_form(self):
        form = self.context.REQUEST.form
        result = {}
        if form.has_key('submitted'):
            submit = form.get('__submit__')
            model, instance = submit.split('+')
            model = form.get('model_override', model)
            
            site_root = self.context.site_root()

            localScripts = getattr(site_root.LocalScripts, 'forms', None)
            oldScripts = getattr(site_root.Scripts, 'forms')
            assert oldScripts, 'Could not get folder Scripts/forms'
             
            modelDir = localScripts and getattr(localScripts, model, 
              getattr(oldScripts, model, None)) or getattr(oldScripts, model, None)
            if modelDir:
                assert hasattr(modelDir, model)
                if hasattr(modelDir, instance):
                    script = getattr(modelDir, instance)
                    assert script
                    retval = script()
                    return retval
                else:
                    m = """<p>Could not find the instance
                           <code>%s</code> in the model
                           <code>%s</code>.</p>""" % (instance, model)
                    result['error'] = True
                    result['message'] = m
            else:
                m = """<p>Could not find the model 
                       <code>%s</code>.</p>""" % model
                result['error'] = True
                result['message'] = m
            assert result.has_key('error')
            assert result.has_key('message')
            assert result['message'].split
    
        result['form'] = form            
        return result

    # To be converted: Scripts.get_firstLevelFolder(context)

class GSUnknownError(BrowserView):
    index = ZopeTwoPageTemplateFile('browser/templates/unknown_error.pt')
    def __call__(self, *args, **kw):
        self.request.response.setHeader('Content-Type', 'text/html; charset=UTF-8')
        # should this really be a 500, that suggests a server error?
        #self.request.response.setStatus(500)
        return self.index(self, *args, **kw)

InitializeClass( GSContentView )

