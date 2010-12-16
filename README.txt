Introduction
============

The code in this product is responsible for displaying the content-pages
on GroupServer: what we call the "pragmatic templates". It controls
the basic layout of the XHTML 1.0 pages, and contains the core CSS, and
the JavaScript that we use everywhere.

Page Structure
==============

The page structure us defined using two files. Each file defines *slots*
that are filled by other products, using `the Zope METAL system`_. The
file ``browser/skin/groupserver_layout.pt`` lays out the pages with
a context-menu. Pages without a context menu (full-width pages) are
arranged by ``browser/skin/groupserver_site_home_layout.pt``

Slots
-----

There are ten slots defined. Only the title and body of the page are
required, as shown in the table below.

=====================  ========  =================================================
Name                   Required  Note
=====================  ========  =================================================
``title``              **True**  Normally the ``<title>`` element.
``metadata``           False     Page metadata, such as ``<link>`` elements.
``style``              False     A page specific ``<style>`` element.
``search``             False     A page-specific search box.
``sitenavigation``     False     A page-specific site navigation menu (main menu).
``utilitylinks``       False     Login, Logout and Profile links.
``contextnavigation``  False     The context menu.
``body``               **True**  The body of the page.
``footer``             False     The page footer.
``javascript``         False     The JavaScript for the page.
=====================  ========  =================================================

Most of the slots — ``search``, ``sitenavigation``, ``utilitylinks``,
``contextnavigation`` and ``footer`` — are filled automatically. A page
will only have to fill them when the user must be *overdetermined*. For
example, most of the menus are hidden during sign-up (see
``gs.profile.signup``).

The ``style`` and ``javascript`` slots are used to over-ride the default
behaviour of the page. Both slots appear *after* the default code is
added to the page.

Style Sheet
===========

The CSS layout is based on an 18px rhythm, with all measurements 
specified in ems. Below is a table that can be used to convert 
between units, pixels and ems. (All measurements should be multiples
of half-units).

+-------+-----+-------+
| Units | px  |  em   |
+=======+=====+=======+
|  0.5  |   9 | 0.692 |
+-------+-----+-------+
|  1.0  |  18 | 1.385 |
+-------+-----+-------+
|  1.5  |  27 | 2.077 |
+-------+-----+-------+
|  2.0  |  36 | 2.769 |
+-------+-----+-------+
|  2.5  |  45 | 3.467 |
+-------+-----+-------+
|  3.0  |  54 | 4.154 |
+-------+-----+-------+
|  3.5  |  63 | 4.846 |
+-------+-----+-------+
|  4.0  |  72 | 5.538 |
+-------+-----+-------+
|  4.5  |  81 | 6.231 |
+-------+-----+-------+
|  5.0  |  90 | 6.923 |
+-------+-----+-------+
|  5.5  |  99 | 7.615 |
+-------+-----+-------+
|  6.0  | 108 | 8.307 |
+-------+-----+-------+

For values above 6u use the following formula::

       u × 18.0
  em = ────────
         13.0

Colour
------

No colour is specified in this stylesheet. Instead just black, white, and
a little grey is used. Two skins ``gs.skin.blue`` and ``gs.skin.green``
provide colour on top of the layout specified in this product.

Authors
=======
`Ben Ford <ben@metasoltuions.co.nz>`_ did the initial design work. The
CSS coding and egg creation was by `Michael JasonSmith 
<mpj17@onlinegroups.net>`_.

.. _The Zope METAL system: http://wiki.zope.org/ZPT/METAL

