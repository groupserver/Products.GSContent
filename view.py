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
        
    def get_id(self):
        assert self.siteObj
        retval = self.siteObj.getId()
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
    def get_site_info(self):
        return Products.GSContent.interfaces.IGSSiteInfo(self.context)

    def process_form(self):
        form = self.context.REQUEST.form
        result = {}
        if form.has_key('submitted'):
            submit = form.get('__submit__')
            model, instance = submit.split('+')
            model = form.get('model_override', model)
            
            oldScripts = self.context.Scripts.forms
            if hasattr(oldScripts, model):
                modelDir = getattr(oldScripts, model)
                if hasattr(modelDir, instance):
                    script = getattr(modelDir, instance)
                    assert script
                    retval = script()
                    #retval['form'] = form
                    return retval
                else:
                    m = """<p>Could not find the instance
                           <code>%s</code></p>.""" % instance
                    result['error'] = True
                    result['message'] = m
            else:
                m = """<p>Could not find the model 
                       <code>%s</code></p>.""" % model
                result['error'] = True
                result['message'] = m
            assert result.has_key('error')
            assert result.has_key('message')
            assert result['message'].split
    
        result['form'] = form            
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
