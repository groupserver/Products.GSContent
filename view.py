'''GroupServer-Content View Class

This does not do anything yet; I created it to remind myself to do something
hoopy later.
'''
import sys, re, datetime, time
import Products.Five, DateTime, Globals
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class GSView(Products.Five.BrowserView):
    pass
    
    # First one to be converted: Scripts.get_firstLevelFolder(context)

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

Globals.InitializeClass( GSView )
