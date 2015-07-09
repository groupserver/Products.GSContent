Changelog
=========

16.2.0 (2015-07-08)
-------------------

* Handling HTTPS in the ``SiteInfo.get_url`` method, closing `Issue 4171`_

.. _Issue 4171: https://redmine.iopen.net/issues/4171

16.1.4 (2015-05-06)
-------------------

* Ensuring the site name is Unicode

16.1.3 (2014-10-09)
-------------------

* Naming the reStructuredText files as such
* Pointing to GitHub_ as the canonical repository
* Updating the product metadata
* Removing old code

.. _GitHub: https://github.com/groupserver/Products.GSContent

16.1.2 (2014-04-04)
-------------------

* Making the ``SiteInfo`` class inherit from ``object`` (new-style)
* Adding a check for the context

16.1.1 (2013-11-27)
-------------------

* Cleaning up the code

16.1.0 (2013-05-30)
-------------------

* Following the moving of jQuery UI to `gs.content.js.jquery.ui`_

.. _gs.content.js.jquery.ui: https://github.com/groupserver/gs.content.js.jquery.ui

16.0.0 (2013-04-02)
-------------------

* Moving the disable-submit code to `gs.content.form`_
* Moving the crypto library to `gs.login`_
* Cleaning up the code

.. _gs.login: https://github.com/groupserver/gs.login
.. _gs.content.form: https://github.com/groupserver/gs.content.form

15.0.0 (2013-02-13)
-------------------

* Moving the disclosure button to `gs.content.js.disclosure`_

.. _gs.content.js.disclosure: https://github.com/groupserver/gs.content.js.disclosure

14.0.1 (2012-08-06)
-------------------

* Silencing some errors with sites that do not exist

14.0.0 (2012-08-02)
-------------------

* Moving the layout templates to `gs.content.layout`_

.. _gs.content.layout: https://github.com/groupserver/gs.content.layout

13.0.2 (2012-06-04)
-------------------

* Updating the CSS version number

13.0.1 (2012-05-16)
-------------------

* Updating the CSS version number

13.0.0 (2012-02-14)
-------------------

* Moving the site homepage to `gs.site.home`_

.. _gs.site.home: https://github.com/groupserver/gs.site.home 

12.0.0 (2011-07-14)
-------------------

* Moving the CSS to `gs.content.css`_

.. _gs.content.css: https://github.com/groupserver/gs.content.css

11.1.0 (2011-04-15)
-------------------

* Adding the CSS for hiding posts

11.0.5 (2011-04-06)
-------------------

* Updating the CSS

11.0.4 (2011-03-31)
-------------------

* Fixing the ``<base>`` element

11.0.3 (2011-03-08)
-------------------

* Adding a ``pdflink`` class and icon

11.0.2 (2011-02-21)
-------------------

* Fixing the radio buttons
* Fixing the check buttons
* Refactoring the CSS for the *Image* page

11.0.1 (2011-01-28)
-------------------

* Updating to jQuery 1.4.4

11.0.0 (2010-12-20)
-------------------

* New GroupServer layout, based on a design by MetaSolutions

10.0.1 (2010-10-21)
-------------------

* Fixing the ``<base>`` element

10.0.0 (2010-10-12)
-------------------

* Adding a favicon
* Adding a global metadata slot
* Moving the ``jQuery`` code to `gs.content.js.jquery.base`_

.. _gs.content.js.jquery.base: https://github.com/groupserver/gs.content.js.jquery.base


9.1.2 (2010-09-08)
------------------

* Marking the profile page as current when viewing the profile

9.1.1 (2010-08-31)
------------------

* Allowing legacy (ZMI) code to work

9.1.0 (2010-08-12)
------------------

* Fixing acquisition (!)
* Dealing with HTML in disclosure headings

9.1.0 (2010-08-04)
------------------

* Adding a method to the site-info to list the site administrators

9.0.0 (2010-08-02)
------------------

* Adding the *sharebox* CSS
* Moving the groups code to `gs.groups`_

.. _gs.groups: https://github.com/groupserver/gs.groups


8.4.1 (2010-07-09)
------------------

* Updating for Zope 2.13

8.4.0 (2010-05-25)
------------------

* Updating the CSS: print CSS, and font-reset

8.3.0 (2010-04-27)
------------------

* Adding a look-up for the canonical port

8.2.0 (2010-04-23)
------------------

* Updating the JavaScript
* Updating the configuration file

8.1.0 (2010-04-01)
------------------

* Updating the CSS: making the site memberships beautiful

8.0.1 (2010-03-08)
------------------

* Getting the groups and sites to line up on the *Profile* page

8.0.0 (2010-01-25)
------------------

* Moving the 404 to `gs.errormesg`_

.. _gs.errormesg: https://github.com/groupserver/gs.errormesg

7.4.1 (2009-12-30)
------------------

* Updating the CSS

7.4.0 (2009-12-17)
------------------

* Adding the ``dataTables`` plugin

7.3.0 (2009-11-24)
------------------

* Making the *submit* button disable when someone clicks on it

7.2.0 (2009-11-17)
------------------

* Updating ``jQuery``
* Updating the CSS

7.1.1 (2009-11-05)
------------------

* Fixing the disclosure button

7.1.0 (2009-10-14)
------------------

* Fixing a Unicode issue
* Updating the CSS
* Adding autoversioning

7.0.0 (2009-10-05)
------------------

* Rearranged into egg-form

6.3.0 (2009-09-02)
------------------

* Updating the CSS
* Making the cache quieter

6.2.2 (2009-06-26)
------------------

* Updating the help

6.2.1 (2009-06-11)
------------------

* Updating the CSS

6.2.0 (2009-05-28)
------------------

* Adding drag and drop support

6.1.2 (2009-05-14)
------------------

* Updating the cache key for the groups

6.1.1 (2009-04-30)
------------------

* Updating the ``jQuery`` library
* Ensuring all pages output ``text/html``

6.1.0 (2009-02-18)
------------------

* Adding a link to email support from the *Not found* page
* Moving the CSS for the tabs out of the HTML and into the global stylesheet

6.0.5 (2008-12-12)
------------------

* Fixing a CSS issue
* Trying to make Microsoft Internet Explorer behave

6.0.4 (2008-11-11)
------------------

* Removing an assert
* Improving the documentation

6.0.3 (2008-10-21)
------------------

* Making the pages more compliant with the HTML specification
* Changing the content type to ``text/html``

6.0.2 (2008-10-06)
------------------

* Using a better cache-key

6.0.1 (2008-10-02)
------------------

* Improving the sorting of group names
* Performance and speed improvements

6.0.0 (2008-09-26)
------------------

* Moving the group-info class to ``GSGroup``

5.10.1 (2008-09-18)
-------------------

* Updating the CSS

5.10.1 (2008-09-12)
-------------------

* Updating the site homepage
* Updating the CSS

5.10.0 (2008-09-05)
-------------------

* Creating the distinction between the site name and site title
* Adding support for images at the bottom of posts
* Adding previous and next links to the *Image* page
* Updating the CSS

5.9.4 (2008-08-26)
------------------

* Decreasing the size of the text-entry boxes
* Fixing some errors

5.9.3 (2008-08-14)
------------------

* Allowing the ZMI-side code access the site-info class

5.9.2 (2008-07-31)
------------------

* Fixing an error

5.9.1 (2008-07-15)
------------------

* Making the 404s actually 404

5.9.0 (2008-06-19)
------------------

* Updating the CSS
* Refactoring the utility links
* Improving the redirecting when logging in or logging out

5.8.1 (2008-06-06)
------------------

* Static content publisher handles published revision-id

5.8.0 (2008-06-01)
------------------

* Adding caching
* Allowing Zope 2 ZMI-side code to access the group-info class
* Updating the CSS
* Fixing the size of the radio-buttons

5.7.0 (2008-05-17)
------------------

* Updating the CSS
* Removing the breadcrumbs
* Fixing the layout of radio-buttons created by ``zope.formlib``
* Fixing references to ``division_object``o

5.6.1 (2008-04-23)
------------------

* Updating the CSS
* Making membership of a private group visible to another member
  of that same private group

5.6.0 (2008-04-18)
------------------

* Adding site-wide notification support
* Updating the CSS
* Changing the way the ``forms`` folder is assigned

5.5.0 (2008-04-02)
------------------

* Adding the ``get_property`` method to the site-info class

5.4.1 (2008-03-26)
------------------

* Fixing the context menu
* Dealing with issues

5.4.0 (2008-03-10)
------------------

* Making the title of the site clickable
* Updating the JavaScript disclosure library, so it can handle
  buttons starting off open
* Making some tweaks

5.3.2 (2008-01-30)
------------------

* Making some tweaks

5.3.1 (2007-12-20)
------------------

* Updating the CSS, fixing the forms

5.3.0 (2007-12-11)
------------------

* Updating the API for the ``GroupInfo`` class
* Getting a list of groups the person can join

5.2.0 (2007-12-05)
------------------

* Fixing some security
* Updating the CSS
* Removing the ``http://`` from the start of URLs
* Adding a view of email notifications

5.1.0 (2007-11-19)
------------------

* Updating the CSS and icons
* Adding an experimental three-column layout for the site homepage
* Adding ``toggle_all``, ``show_all`` and ``hide_all`` to the
  ``GSDisclosureButton`` JavaScript "module"
* Fixing some links

5.0.1 (2007-11-01)
------------------

* Cleaning up the old CSS

5.0.0 (2007-10-05)
------------------

* Adding the ``jQuery`` JavaScript library
* Removing the ``Protoype`` JavaScript library
* Allowing skinning to occur

4.1.3 (2007-08-30)
------------------

* New CSS for the search results

4.1.2 (2007-08-21)
------------------

* Fixing the margins around the ``<h2>`` element

4.1.1 (2007-08-17)
------------------

* Tweaking the CSS
* Fixing an error with Microsoft Internet Explorer on the site
  homepage
* Altering the grid used in the CSS

4.1.0 (2007-08-10)
------------------

* Using sprites for the file icons
* Refactoring the CSS
* Using ``protopacked``
* Removing old libraries

4.0.0 (2007-07-31)
------------------

* Performance improvements

  + Using version numbers for the JavaScript files
  + Using the sprites file
  + Moving all the JavaScript to the bottom of the page

* Using the new CSS
* Altering the search-slot
* Adding GIF-images for the orange, black, and green themes

3.2.2 (2007-07-20)
------------------

* Fixing the security
* Stopping the JavaScript from being loaded by the wrong pages

3.2.1 (2007-07-13)
------------------

* Adding some animations
* Refactoring the order that the JavaScript is loaded
* Fixing the permissions

3.2.0 (2007-06-19)
------------------

* Adding Prototype to all the pages
* Adding support for the disclosure button 

3.1.1 (2007-06-05)
------------------

* Cleaning up the code

3.1.0 (2007-06-28)
------------------

* Adding some factories for the site-info and group-info classes

3.0.0 (2007-05-11)
------------------

* Adding the ``GroupInfo`` class

2.2.1 (2007-04-13)
------------------

* Setting the default viewable for ``OFS.Folder.Folder``

2.2.0 (2007-03-30)
------------------

* Adding support for ``LocalScripts``
* Full-screen pages now full-screen
* Fix for Apple Safari and KDE Konqueror

2.1.1 (2007-02-28)
------------------

* Cleaning up the code

2.1.0 (2007-02-08)
------------------

* Cleaning up the error pages
* Removing ``dojo``
* Adding a JS date  library
* Adding the pane-code

2.0.0 (2007-02-02)
------------------

* Adding support for stylesheets in ``PresentationCustom``
* Adding icons
* Adding more robust footers
* Adding the ``prototype`` and ``scriptaculous`` JavaScript libraries
* Adding the JavaScript crypto library
* Refactoring the ``gst_site_info`` and ``get_group_info`` into
  ``@properties`` of the view
* Removing ``local.css``

1.2.0 (2006-12-06)
------------------

* Adding the full-page layout

1.1.0 (2006-11-24)
------------------

* Adding support for styling the site homepage
* Updating the layout
* Adding ``IGSSiteInfo`` as an adaptor

1.0.3 (2006-11-16)
------------------

* Making the resource URIs absolute, so they are cached better
* Adding some placeholder package files to prevent *Not found* redirects
* Removed the automatic setting of the ``id`` attribute on the
  ``<body>`` element of the page
* Fixing links

1.0.2 (2006-11-08)
------------------

* Passing the site name into the view

1.0.1 (2006-10-31)
------------------

* Hiding the popup help code from Microsoft Internet Explorer
* Cleaning up the JavaScript so it works in Mozilla Firefox and Opera

1.0.0 (2006-10-23)
------------------

Initial version. Prior to the creation of this product the page
templates were handled by `Products.GroupServer`_

.. _Products.GroupServer: https://github.com/groupserver/Products.GroupServer

..  LocalWords:  Changelog Refactoring stylesheet sharebox
..  LocalWords:  jQuery jquery favicon reStructuredText GitHub
..  LocalWords:  GSContent
