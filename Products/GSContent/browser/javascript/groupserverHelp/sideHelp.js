// GroupServer Popup Help JavaScript Code
//
// DESCRIPTION
//   This should-be-a-class handles the popup-help code used on the 
//   GroupServer pages. It uses the Dojo JavaScript library to create the 
//   popup-window widget, and perform the XMLHTTPRequest. 
//

//Dojo require statements
dojo.require("dojo.io.*" );
dojo.require("dojo.dom.*" );
dojo.require("dojo.event.*");
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
groupserverHelp__currentSectionId = '';

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
 
  if (helpSectionId == groupserverHelp__currentSectionId)
  {
      return;
  }
  groupserverHelp__currentSectionId = helpSectionId;

  
  if (groupserverHelp__window == null)
  {
      groupserverHelp__window = groupserverHelp_create_window();
  }
  groupserverHelp_show_window();
  
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
    },
    errror: function(type, errror) {
      groupserverHelp_loadError(error, groupserverHelp__window);
    }
  });
};

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
    var d = document.createElement("div");
    d.setAttribute("id", "helpPane");
    d.setAttribute("class", "sideHelpHiddenMode");
    
    var s = document.createElement("span");
    s.setAttribute("id", "helpPaneTitleBar");
    d.appendChild(s);
   
    var h = document.createElement("h2");
    h.setAttribute("id", "helpPaneLabel");
    h.appendChild(document.createTextNode("Help"));
    s.appendChild(h);

    var close = document.createElement("span");
    close.setAttribute("id", "helpPaneClose");
    close.setAttribute("onclick", "groupserverHelp_hide_window()");
    s.appendChild(close)

    var helpContent = document.createElement("div");
    helpContent.setAttribute("id", "helpPaneContent")
    d.appendChild(helpContent);
         
    var content = document.getElementById("content");
    content.insertBefore(d, content.firstChild);
    return d;
}

groupserverHelp_show_window = function() {
    var helpPane = document.getElementById("helpPane");
    helpPane.setAttribute("class", "sideHelpHelpMode");
    
    var p = document.createElement("p");
    p.setAttribute("id", "helpPaneLoadingText");
    p.appendChild(document.createTextNode("Loading help\u2026"));

    var helpPaneContent = document.getElementById("helpPaneContent");
    if (helpPaneContent.childNodes.length > 0) 
    {
        helpPaneContent.replaceChild(p, helpPaneContent.childNodes[0]);
    }
    else
    {
        helpPaneContent.appendChild(p);
    }
    var content = document.getElementById("content");
    content.setAttribute("class", "contentHelpMode");
}

groupserverHelp_hide_window = function() {
    groupserverHelp__currentSectionId = '';
    var helpPane = document.getElementById("helpPane");
    helpPane.setAttribute("class", "sideHelpHiddenMode");
    var content = document.getElementById("content");
    content.setAttribute("class", "contentSideHelpHidden");
    
    var helpPaneContent = document.getElementById("helpPaneContent");
    if (helpPaneContent.childNodes.length != 0)
    {
        for (var i=0; i < helpPaneContent.childNodes.length; i++)
        {
            helpPaneContent.removeChild(helpPaneContent.childNodes[i]);
        }
    }  
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
    //try 
    //{
        var originalSection = data.getElementById(sectionId);
  
        var titleId = sectionId + "-t";
        var titleNode = data.getElementById(titleId);
        
        var label = document.getElementById("helpPaneLabel");
        titleChild0 = titleNode.childNodes[0];
        labelChild0 = label.childNodes[0];
        label.childNodes[0].data = titleNode.childNodes[0].data;

        //originalSection.removeChild(titleNode);
        var section = groupserverHelp_get_fixed_section(originalSection);
    
        var p = groupserverHelp_create_more_link(sectionId);
        section.appendChild(p);
//    }
    //catch (e)
    //{
     //   var m = "the section <q>" + sectionId + "</q> could not be loaded ";
       // m = m + "<code>(" + e + ")</code>";
        //groupserverHelp_loadError(m, w);
        //return;
    //}
    var helpPaneContent = document.getElementById("helpPaneContent");
    helpPaneContent.replaceChild(section, helpPaneContent.childNodes[0]);
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
groupserverHelp_add_popup_to_helpLink = function() {
    var helpLinks = groupserverHelp_getElementsByClass(document.body,
                                                       "helpLink", "a");
    for(var i = 0; i < helpLinks.length; i++)
    {
        var section = helpLinks[i].href.split("#",2)[1];
        var url = "javascript:groupserverHelp_popup('"+ section+"')";
        helpLinks[i].href = url;
    }
}

// Call "add_popup_to_helpLink" when the page loads.
if (!dojo.render.html.ie)
{
    dojo.addOnLoad(groupserverHelp_add_popup_to_helpLink);
}

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


groupserverHelp_loadError = function (error, w) 
{
  var m = "<p>There was an error loading the context-sensitive help: "
  m = m + error + ". This is a bug, please contact ";
  m = m + '<a class="email" title="OnlineGroups.Net Support" '
  m = m + 'href="mailto:support@onlinegroups.net">support@onlinegroups.net</a>, '
  m = m + "sending the contents of this window with your message. "
  m = m + "Thank you.</p>" 
  alert(m);
}