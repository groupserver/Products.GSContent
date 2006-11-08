from zope.interface.interface import Interface
class IFolder(Interface):
    pass

class IGSContentFolder(Interface):
    """A folder that displays static (or near-static) content on a 
    GroupServer site"""

    def get_site_info():
          """Get information about the current GroupServer site
          
          ARGUMENTS
              None.
              
          RETURNS
              An object that implements the "IGSSiteInfo" interface.
          
          SIDE EFFECTS
              None.
          """
          pass
          
    def process_form():
        """process_form: Process the submitted faux-XForms form.
        
        DESCRIPTION
           The "process_form" method takes an XHTML1 form and determines
           the method of "", or the external script, that should be
           run. This takes the hassle out of specifying, in Web pages,
           which script should be run, as "process_form" determines it
           based on the submitted faux-XForms model and faux-XForms 
           submission method.
        
        ARGUMENTS
          None, technically. The HTML form, ".context.REQUEST.form"
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
          ".context.Scripts.forms": The folder that contains
              the scripts that should be run, if the appropriate
              callback cannot be found in ""
        """
        pass

class IGSSiteInfo(Interface):
    """GroupServer Site Information Interface
    
    GroupServer sites, nee "divisions", are the highest-level of
    group organisation on GroupServer: every group must belong to one
    (and only one) site. The "IGSSiteInfo" interface defines the 
    mechanism for getting useful information about the site.
    
    For the most-part, the IGSSiteInfo implementations replace the 
    "division" scripts, located in "Products/GroupServer/Scripts/get/"
    in GroupServer 0.9./ 
    """
    def get_id():
        """Get the ID of the site.
       
        ARGUMENTS
            None.
            
        RETURNS
            A string, containing the site ID.
            
        SIDE EFFECTS
            None.
        """
        pass


    def get_name():
        """Get the name of the site.
       
        ARGUMENTS
            None.
            
        RETURNS
            A string, containing the name of the site.
            
        SIDE EFFECTS
            None.
        """
        pass
    
    def get_url():
        """Get the URL, which can be used to retrieve the site homepage
        
        The URL of the site can be used to form other URLs on the site, or
        simply as a link to the homepage of the site. 
        
        ARGUMENTS
            None.
        
        RETURNS
            A string, containing the URL of the site homepage without a
            trailing "/". If the "canonicalHost" property of the division
            configuration is set, then the full URL is returned, including
            the "http://" and the host-name. Otherwise, only the absolute
            URL, beginning with a "/" is returned.
            
        SIDE EFFECTS.
            None.
        """
        pass
