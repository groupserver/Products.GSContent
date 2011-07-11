Introduction
============

The code in this product is responsible for displaying the content-pages
on GroupServer: what we call the "pragmatic templates". It controls
the basic layout of the XHTML 1.0 pages, and the JavaScript that we
use everywhere.

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

.. _The Zope METAL system: http://wiki.zope.org/ZPT/METAL

