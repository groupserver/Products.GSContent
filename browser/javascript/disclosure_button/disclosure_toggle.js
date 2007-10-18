// Functions for handling the disclosure buttons.
GSDisclosureButton = function () {
    /* GroupServer Disclosure Button Module.
    
        A disclosure button consists of a 
    
        Functions
        
        "init"   Add arrows to all the disclosure buttons, and
                 attach a click callback.
    */

    // Private variables
    // Arrows
    var hiddenArrow = "\u25b6";
    var shownArrow = "\u25bc";
    var NBSP = "\u00a0";
    // Elements of the disclosure widgets
    var dw = ".disclosureWidget";
    var db = ".disclosureButton";
    var dsh = ".disclosureShowHide";

    // Private methods
    var buttonClicked = function () {
        text = jQuery(this).text()
        coreText = text.substring(2, text.length);
        arrow = text.substring(0, 1);
        showHideWidget = jQuery(this).parents(dw).find(dsh)
        
        if ( arrow == hiddenArrow ) {
            jQuery(this).text(shownArrow+NBSP+coreText);
        } else {
            jQuery(this).text(hiddenArrow+NBSP+coreText);
        }
        showHideWidget.slideToggle("slow");
    }
    
    // Public methods and properties
    return {
        init: function () {
            jQuery(db).prepend(hiddenArrow+NBSP);
            jQuery(db).removeAttr('href').css("cursor","pointer");
            jQuery(db).click( buttonClicked );
        }
    };
}(); // GSDisclosureButton

jQuery(document).ready( function () {
    GSDisclosureButton.init(); 
});

