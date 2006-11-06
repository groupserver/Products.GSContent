'''GroupServer-Content View Class
'''
import sys, re, datetime, time
import Products.Five, DateTime, Globals
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
import zope.interface
import Products.GSContent.interfaces

class GSSiteInfo:
    """An implementation of the GroupServer Site Information Interface
    
    This adaptor provides information about the site, based on the context
    of the object.
    """
    zope.interface.implements(Products.GSContent.interfaces.IGSSiteInfo)
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
        assert context
        
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
        assert self.context
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
        retval = retval.aq_inner.aq_explicit
        assert retval 
        assert hasattr(retval, markerAttr)
        assert getattr(retval, markerAttr)
        return retval
                
    def __get_site_config(self):
        """Get the site configuration instance from the site object.
        
        ARGUMENTS
            None.
        
        RETURNS
            The site configuration instance.
            
        SIDE EFFECTS
            None.
            
        ENVIRONMENT
            "self.siteObject": The site object."""
        assert self.siteObj
        retval = getattr(self.siteObj, 'DivisionConfiguration', None)
        assert retval
        return retval
        
    def get_name(self):
        assert self.config
        
        retval = self.config.getProperty('siteName')
        if not retval:
            retval = self.siteObj.title_or_id()
            
        assert retval
        return retval
        
    def get_url(self):
        assert self.siteObj
        assert self.config
        retval = ''
        cannonicalHost = self.config.getProperty('canonicalHost', '')
        if cannonicalHost:
            retval = 'http://%s' % cannonicalHost
        else:
            retval = '/%s' % self.siteObj.absolute_url(1)

        assert retval
        return retval

class GSContentView(Products.Five.BrowserView):
    '''View object for standard GroupServer content objects'''
    
    def __init__(self, context, request):
          Products.Five.BrowserView.__init__(self, context, request)
          self.__set_site_info(GSSiteInfo(context))

    def __set_site_info(self, siteInfo):
          assert siteInfo
          assert Products.GSContent.interfaces.IGSSiteInfo.providedBy(siteInfo)
          self.__siteInfo = siteInfo
          assert self.__siteInfo
           
    def get_site_info(self):
          assert self.__siteInfo
          retval = self.__siteInfo
          assert retval
          return retval

    def process_form(self):
        form = self.context.REQUEST.form

        result = {'error': True, 
        'message': '<p>The form had errors.</p>',
        'form': form}

        if not form.get('submitted', False):
            return {}

        model, submission = form.get('__submit__').split('+')
        model = form.get('model_override', model)

        oldForms = self.context.Scripts.forms
        
        if hasattr(self, model):
            cb = getattr(self.model, submission)
            result = cb()
        elif hasattr(oldForms.aq_explicit, model):
            cb_container = getattr(oldForms.aq_explicit, model)
            cb = getattr(cb_container, submission)
            result = cb()
        else:
            result['error'] = True
            m = '''<p>Could not find the form for the model <code>%s</code>, 
              and the submission <code>%s</code>. 
              This should not have happened, please contact
              <a title="OnlineGroups.Net Support" 
                href="mailto:support@onlinegroups.net" 
                class="email">support@onlinegroups.net</a>.</p>''' \
              % (model, submission)
            result['message'] = m
        
        # Add the form to the result.    
        result['form'] = form
                
        assert result.has_key('error')
        assert result.has_key('message')
        assert result['message'].split
        return result
    
    # To be converted: Scripts.get_firstLevelFolder(context)

class GSNotFoundError(Products.Five.BrowserView):
    index = ZopeTwoPageTemplateFile('browser/templates/not_found.pt')
    # make the template publishable
    def __call__(self, *args, **kw):
        self.request.response.setStatus(404)
        return self.index(self, *args, **kw)

class GSUnknownError(Products.Five.BrowserView):
   index = ZopeTwoPageTemplateFile('browser/templates/unknown_error.pt')
   def __call__(self, *args, **kw):
       # should this really be a 500, that suggests a server error?
       #self.request.response.setStatus(500)
       return self.index(self, *args, **kw)

Globals.InitializeClass( GSContentView )
