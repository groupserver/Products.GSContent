// GroupServer module for disabling submit buttons when clicked. This
//  stops a user hammering on the button, and provides some feedback.
jQuery.noConflict();
var GSDisableSubmit = function () {
    /* GroupServer Disable Submit
    
    FUNCTIONS
      "init":   Add the callbacks to the entry widgets
    
    */

    // Private variables
    // The disabled  button that says "Processing", followed by
    //    ellipsis.
    var newButtonText = '<input class="processing button" type="button" disabled="disabled" value="Processing\u2026"/>';
    
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
        // --=mpj17=-- If I disable the button the form is not 
        //      processed by zope.formlib, as disabled buttons are
        //      "unsuccessful" by definition, so they are not POSTed
        //      to Zope as part of the form data. So, I *hide* the
        //      button (using CSS) and add a disabled button in its
        //      place.
        var s = null;
        s = jQuery(submitButton);
        s.before(newButtonText);
        s.addClass('hiddenType');
        s.css('display', 'none');
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

