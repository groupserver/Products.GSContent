// GroupServer Popup Help JavaScript Code
//
// DESCRIPTION
//   This should-be-a-class handles the popup-help code used on the 
//   GroupServer pages. It uses the Dojo JavaScript library to create the 
//   popup-window widget, and perform the XMLHTTPRequest. 
//

//Dojo require statements
dojo.require("dojo.io.*" );
//dojo.require("dojo.XML.*" );
dojo.require("dojo.dom.*" );
dojo.require("dojo.widget.*" );
dojo.require("dojo.event.*");
dojo.require("dojo.widget.LayoutContainer"); 
dojo.require("dojo.widget.FloatingPane" );
//all dojo.require above this line
dojo.require();

// Constants
// * The "pretty" manual page, with all the navigation and stylesheets.
groupserverHelp_PrettyURL = 'help/manual/';
// * The basic page, which loads quickly
groupserverHelp_BaseURL = 'help/manual/raw.html';

// Globals 
// * The ID of the section we are trying to load 
groupserverHelp_LoadingSection = '';
// * Internal variable: set to true if we are loading a page. 
groupserverHelp__isLoading  = false;
groupserverHelp__window  = null;

// popup: Popup the help for a particular section
//
// This is the main interface for the popup-help. It takes the ID of the
// section to display, and sets up and "dojo.io.bind" request to grab the
// data, using an HTTP GET. After the data has been recieved, the section
// is displayed by calling "help_section".
//
// This code can only be called again *after* some help has been loaded.
//
// ARGUMENTS
//    "helpSectionId": The ID of the section to display from the help.
//
// RETURNS
//    None.
//
// SIDE EFFECTS
//    Calls "display_help_section", which displays the help pane.
//
groupserverHelp_popup = function (helpSectionId) {
  //netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserRead");
  //netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");

  if (groupserverHelp_isLoading())
  {
    return;
  }
  
  if (groupserverHelp__window == null)
  {
      groupserverHelp__window = groupserverHelp_create_window();
  }
  else
  {
      document.body.appendChild(groupserverHelp__window.domNode);
  }
  groupserverHelp__window.setContent("<p>Loading help-documentation&#8230;</p>");
  
  groupserverHelp_LoadingSection = helpSectionId;
  groupserverHelp_set_loading(true);
    
  dojo.io.bind({
    url: groupserverHelp_BaseURL,
    mimetype: 'text/xml',
    method: "GET",
    transport: "XMLHTTPTransport",
    useCache: 1,
    handler: function(type, data, event) {
      groupserverHelp_display_help_section(data, helpSectionId, 
                                           groupserverHelp__window);
      groupserverHelp_set_loading(false);
      }
    })
}

// isLoading: Is the help code trying to load a page?
// 
// ARGUMENTS
//    None
//
// RETURNS
//    If the code is trying to load a page, "true" is returned, "false"
//    is returned otherwise.
//
groupserverHelp_isLoading = function ()
{
  return groupserverHelp__isLoading;
}

// set_loading: set weather help is being loaded
// 
// ARGUMENTS
//    "isLoading": a boolean, set to "true" if help is being loaded
//
// RETURNS
//    None.
//
// SIDE EFFECTS
//    "groupserverHelp__isLoading" is set to the value of "isLoading".
//
groupserverHelp_set_loading = function (isLoading) 
{
  groupserverHelp__isLoading = isLoading;
}

// create_window: Create the Dojo floating pane widget for the popup help
//
// ARGUMENTS
//   None.
//
// RETURNS
//   A "dojo.widget.FloatingPane" widget.
//
// SIDE EFFECTS
//   The widget is added to the "document" DOM, and displayed.
//
groupserverHelp_create_window = function () 
{
  var properties = {
    title:"Help", widgetId: "helpPane",
    displayMaximizeAction: 0, displayMinimizeAction:0, displayCloseAction:1,
    constrainToContainer: 0, resizable: 1, doLayout: 1, cacheContent: 1,
    hasShadow: 1, titleBarDisplay:"fancy", windowState:"normal",
    // The ratio betwen width and height is golden
    width:"600px", height:"371px"
   };
   // Uncomment the next two lines of code to use the replacement 
   //    widget-creation method.
   d = document.getElementById("replacedHelpPane");
   d.setAttribute("style", "width: 600px; height: 371px;");
   var w = dojo.widget.createWidget("FloatingPane", properties, d);
      
   // Uncomment the next two lines of code to use the DOM append 
   //    widget-creation method.
   //var w = dojo.widget.fromScript("FloatingPane", properties);
   //document.body.appendChild(w.domNode);
   return w;
}


// display_help_section: Display the section of the online help.
//
// The help section, as returned by the server, is not in a an optimal
// state, as the links will go to the wrong place, and there is no link
// to the full manual. This function fixes the section, before adding it
// to the popup-window.
//
// ARGUMENTS
//   "data":      The data that is returned by "dojo.io.bind". This should 
//                be a complete XML document.
//   "sectionId": The ID of the section we wish to display
//   "w":         The Dojo floating pane widget.
//
// RETURNS
//   None.
//
// SIDE EFFECTS
//   * All the anchor tags in the "sectionId" section of "data" have the
//     "href" attribute replace will an absolute-URL, to the pretty version
//     of the help.
//   * A link, reading "Read more in the full manual" is added to the 
//     bottom of the section.
//   * The section is displayed in the Dojo floating pane widget. 
// 
groupserverHelp_display_help_section = function (data, sectionId, w) 
{
    var originalSection = data.getElementById(sectionId);
    titleId = sectionId + "-t"; 
    titleNode = data.getElementById(titleId);
    w.titleBarText.innerHTML = titleNode.childNodes[0].nodeValue;
    originalSection.removeChild(titleNode);
    var section = groupserverHelp_get_fixed_section(originalSection);
    
    p = groupserverHelp_create_more_link(sectionId);
    section.appendChild(p);

    w.setContent(section);
}

// get_fixed_section: Make the links in the section point to the full manual
//
// The anchor elements ("a" tags) in the manual section may be pointing to
// the wrong place. This function changes the anchors so they contain a
// correctly-functioning link to the help manual.
//
// ARGUMENTS
//   "section": The DOM-node that represents the section.
//
// RETURNS
//   A new DOM node, that has the corrected anchor-tags.
//
// SIDE EFFECTS
//   None.
//   
groupserverHelp_get_fixed_section = function (section)
{
    newSection = section.cloneNode(true);
    links = newSection.getElementsByTagName("a");
    for(i = 0; i < links.length; i++)
    {
        oldHref = links[i].getAttribute("href");
        internalLink = oldHref.split("#", 2)[1];
        newHref  = groupserverHelp_PrettyURL+"#"+internalLink;
        links[i].setAttribute("href", newHref);
    }
    return newSection;
}

// create_more_link: Create the link to the full help-manual.
//
// ARGUMENTS
//    "sectionId": The ID of the section to link to. 
//
// RETURNS
//    A paragraph-element, which can be added to a section or page.
//
groupserverHelp_create_more_link = function (sectionId)
{
    p = document.createElement("p");
    
    more = document.createElement("a");
    moreURL = groupserverHelp_PrettyURL+"#"+sectionId;
    href = document.createAttribute("href")
    href.value = moreURL
    more.setAttributeNode(href);
    txt = document.createTextNode("Read more");
    more.appendChild(txt);
    p.appendChild(more);
    
    txt = document.createTextNode(" in the full manual.");
    p.appendChild(txt);
    
    return p;
}

// add_popup_to_helpLink: Add popups to the helpLink anchors
//
// The links to sections within the user manual *should* be marked with
// the "helpLink" class. This is good as it allows the links to function
// correctly when this JavaScript help library has not loaded. However,
// when this library is present, we want to pop-up the help window. So
// this function replaces all the anchor-elements with span-elements that
// pop up the help window, extracting the section-name out of the "href"
// attribute of the anchor element.
//
// ARGUMENTS
//   None.
//
// RETURNS
//   None.
//
// SIDE EFFECTS
//   All anchor-elements, which have "helpLink" as the class, are replaced
//   with spans, also of the "helpLink" class, that have the onclick
//   callback attached to the "popup" method. 
//
groupserverHelp_add_popup_to_helpLink = function () {
  // Get all the anchor-elements that have "helpLink" as the class
  var helpLinks = groupserverHelp_getElementsByClass(document.body,
                                                     "helpLink", "a");
  // For each anchor element
  for(var i=0; i< helpLinks.length; i++)
  {
    // Create a span element
    var span = document.createElement("span");
    var classAttr = document.createAttribute("class");
    classAttr.value = "helpLink";
    span.setAttributeNode(classAttr); 

    // Get the section from the URL and add it to the onclick callback of
    // the span
    var section = helpLinks[i].href.split("#",2)[1];
    var onclick = document.createAttribute("onclick");
    onclick.value = "groupserverHelp_popup('"+ section+"')";
    span.setAttributeNode(onclick);

    // Move all the children of the anchor to the span
    for(var j=0; j<helpLinks[i].childNodes.length; j++)
    {
        span.appendChild(helpLinks[i].childNodes[j]);
    }

    // Replace the anchor with the new span.
    var parent = helpLinks[i].parentNode; 
    parent.replaceChild(span, helpLinks[i]);
  }
}
// Call "add_popup_to_helpLink" when the page loads.
dojo.addOnLoad(groupserverHelp_add_popup_to_helpLink);

// The following (very useful) function was taken from 
//   http://domscripting.com/blog/display/18
// and modified to get rid of the regular expression.
groupserverHelp_getElementsByClass = function (node,searchClass,tag) {
  var classElements = new Array();
  var els = node.getElementsByTagName(tag);
  var elsLen = els.length;
  for (i = 0, j = 0; i < elsLen; i++) {
    if (els[i].className == searchClass) {
      classElements[j] = els[i];
      j++;
    }
  }
  return classElements;
}
