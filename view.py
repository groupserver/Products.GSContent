'''GroupServer-Content View Class
'''
import sys, re, datetime, time
import Products.Five, DateTime, Globals
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class GSContentView(Products.Five.BrowserView):
    '''View object for standard GroupServer content objects'''
    
    def process_form(self):
        '''process_form: Process the submitted faux-XForms form.
        
        DESCRIPTION
           The "process_form" method takes an XHTML1 form and determines
           the method of "self", or the external script, that should be
           run. This takes the hassle out of specifying, in Web pages,
           which script should be run, as "process_form" determines it
           based on the submitted faux-XForms model and faux-XForms 
           submission method.
        
        ARGUMENTS
          None, technically. The HTML form, "self.context.REQUEST.form"
          is examined (looking for the "___submit___" key) to determine
          which script should be run, based on the faux-XForms model and the
          faux-XForms submission method: the submitted XForms model and 
          faux-XForms submission method should be seperated by a "+" 
          character in the "__submit__" string.
          
        RETURNS
          A result dictionary. Normally the dictionary will contain
          three values. 
              The "error" key: A boolean value, set to True if there is
                  an error.
              The "message" key: The message to be displayed, formatted
                  in XHTML1.
              The "form" key: The form that was submitted.
          If the dictionary is empty then the form was not submitted 
          manually (the "submitted" key of the form was set to False).
           
        SIDE EFFECTS
          Too many to be a work of God. The side-effects are caused by
          the methods and scripts that "process_form" calls, rather
          than "process_form".
          
        ENVIRONMENT
          "self.context.Scripts.forms": The folder that contains
              the scripts that should be run, if the appropriate
              callback cannot be found in "self" 
        '''
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
