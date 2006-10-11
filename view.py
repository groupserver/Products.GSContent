'''GroupServer-Content View Class

This does not do anything yet; I created it to remind myself to do something
hoopy later.
'''
import sys, re, datetime, time
import Products.Five, DateTime, Globals
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class GSView(Products.Five.BrowserView):
    def process_form(self):
        result = {}
        
        form = self.context.REQUEST.form
        result['form'] = form

        if not form.get('submitted', False):
            return result

        model, submission = form.get('__submit__')
        # m = '''<p>Submit: %s</p>''' % submit
        # return {'error': False, 'message': m}
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

Globals.InitializeClass( GSView )
