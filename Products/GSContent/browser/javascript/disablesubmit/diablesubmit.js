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
        buttons.each(function(){disable_button(this)});
        return true;
    }
    var disable_button = function(submitButton) {
        jQuery(submitButton).attr('disabled', 'disabled');
        jQuery(submitButton).attr('value', 'Processing\u2026');
    }
    // Public methods and properties
    return {
        init: function ( ) {
            var forms = null;
            forms = jQuery('form');
            forms.submit(handle_submit);
        }
    };
}(); // GSDisableSubmit

jQuery(document).ready( function () {
    GSDisableSubmit.init(); 
});

