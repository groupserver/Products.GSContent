// GroupServer module for disabling submit buttons when clicked. This
//  stops a user hammering on the button, and provides some feedback.
jQuery.noConflict();
var GSDisableSubmit = function () {
    /* GroupServer Disable Submit
    
    FUNCTIONS
      "init":   Add the callbacks to the entry widgets
    
    */

    // Private variables
    var foo = null;
    
    // Private methods
    var handle_submit = function(event) {
        var form = null;
        var buttons = null;
        form = jQuery(this);
        buttons = form.find(':submit');
        buttons.each(function(){disable_button(this);});
        return true;
    }
    var disable_button = function(submitButton) {
        var s = null;
        s = jQuery(submitButton);
        s.attr('value', 'Processing\u2026');
        // --=mpj17=-- If I disable the button the form is not 
        //      processed by zope.formlib. Disabled buttons are
        //      "unsuccessful" by definition, so they are not POSTed
        //      to Zope as part of the form data.
        //s.attr('disabled', 'disabled');
        return true;
    }
    // Public methods and properties
    return {
        init: function ( ) {        
            jQuery('form').submit(handle_submit);
        }
    };
}(); // GSDisableSubmit

jQuery(document).ready( function () {
    GSDisableSubmit.init(); 
});

