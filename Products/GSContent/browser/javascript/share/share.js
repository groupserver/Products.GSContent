// Code to power a very simple slide down widget, for sharing a URL, for example
// a post.

jQuery.noConflict();
jQuery(document).ready ( function() {
  jQuery('.email-link').each(function() {
    jQuery(this).click(function() {
      fullLink = jQuery(this).parents('.share-links').find('.full-link');
      if (fullLink.is(":hidden")) {
        fullLink.slideDown("slow");
      } else {
        fullLink.slideUp("slow");
      }
    });
  });
});
