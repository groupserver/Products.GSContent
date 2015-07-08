# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.component.interfaces import IFactory
from zope.interface import implements, implementedBy
from App.class_init import InitializeClass
from Products.Five import BrowserView
from gs.core import to_unicode_or_bust
from Products.XWFCore import XWFUtils
from .interfaces import IGSSiteInfo


class GSSiteInfoFactory(object):
    implements(IFactory)

    title = u'GroupServer Site Info Factory'
    descripton = u'Create a new GroupServer site information instance'

    def __call__(self, context):
        retval = GSSiteInfo(context)
        return retval

    def getInterfaces(self):
        retval = implementedBy(GSSiteInfo)
        assert retval
        return retval


class GSSiteInfo(object):
    """An implementation of the GroupServer Site Information Interface

    This adaptor provides information about the site, based on the context
    of the object.
    """

    implements(IGSSiteInfo)

    def __init__(self, context):
        """Create an GSSiteInfo instance.

        ARGUMENTS
            "context" The context of the page.

        SIDE EFFECTS
            Sets
              * "self.context" to the context argument,
              * "self.siteObj" to the site-instance, and
              * "self.config" to the site-configuration instance.
        """
        if not context:
            raise ValueError('No context provided: {0}'.format(context))
        self.context = context
        self.siteObj = self.__get_site_object()
        self.config = self.__get_site_config()

    def __get_site_object(self):
        """Get the site-object, which contains the current instance.

        This method preforms a search for the site instance among the
        ancestors of the current object, walking back up the tree looking
        for the object that has the "is_division" property set to "True".

        ARGUMENTS
            None.

        RETURNS
            The site object.

        SIDE EFFECTS
            None.

        ENVIRONMENT
            "self.context": The context of the object.
        """
        retval = self.context
        markerAttr = 'is_division'
        while retval:
            try:
                if getattr(retval.aq_inner.aq_explicit, markerAttr, False):
                    break
                else:
                    retval = retval.aq_parent
            except:
                break

        try:
            retval = retval.aq_inner.aq_explicit
        except AttributeError:
            retval = None
        return retval

    def __get_site_config(self):
        """ Get the site configuration instance from the site object.

        ARGUMENTS
            None.

        RETURNS
            The site configuration instance.

        SIDE EFFECTS
            None.

        ENVIRONMENT
            "self.siteObject": The site object.

        """
        if self.siteObj:
            retval = getattr(self.siteObj, 'DivisionConfiguration', None)
        else:
            retval = getattr(self.context, 'GlobalConfiguration', None)

        return retval

    @Lazy
    def id(self):
        return self.get_id()

    def get_id(self):
        retval = None
        if self.siteObj:
            retval = self.siteObj.getId()
        return retval

    @property
    def name(self):
        r = self.get_name()
        retval = to_unicode_or_bust(r)
        return retval

    def get_name(self):
        try:
            retval = self.config.getProperty('siteName', '')
        except AttributeError:
            retval = ''
        if not retval and self.siteObj:
            retval = self.siteObj.title_or_id()
        return retval

    @property
    def title(self):
        retval = self.config.getProperty('siteTitle', self.name)
        if isinstance(retval, str):
            retval = to_unicode_or_bust(retval)
        return retval

    @Lazy
    def globalConfig(self):
        retval = getattr(self.context, 'GlobalConfiguration', None)
        if retval is None:
            m = 'Could not find "GlobalConfiuration" from {0}'
            msg = m.format(self.config)
            raise ValueError(msg)
        return retval

    def get_option(self, option, default):
        retval = self.config.getProperty(
            option, self.globalConfig.getProperty(option, default))
        return retval

    @Lazy
    def url(self):
        return self.get_url()

    def get_url(self):
        '''Gets the URL from the site.

:returns: The URL for the site.
:rtype: str

The URL is made up of the *scheme*, the *canonical host* and the  *canonical
port*. All can be set by changing properties on the  ``DivisionConfiguration``
object.

Scheme:
    Either ``https`` if the ``useHTTPS`` boolean property is set to ``True``.
    Otherwise ``http`` is used (the default). The ``useHTTPS`` property may
    also be set on the ``GlobalConfiguration`` object, with the site-specific
    configuration over-riding the global configuration.

Host:
    The value of the ``canonicalHost`` property. If not set then ``/`` is used.

Port:
    If the ``canonicalPort`` property is **either** unset, or the **default**
    value for the *scheme*  (``80`` for HTTP, ``443`` for HTTPS) then the port
    is **omitted** from the URL. Otherwise the port is included in the URL. The
    ``canonicalPort`` property may also be set on the ``GlobalConfiguration``
    object, with the site-specific configuration over-riding the global
    configuration.
'''
        # Using HTTPS may be a global setting
        useHTTPS = self.get_option('useHTTPS',  False)
        # Host is site-specific
        host = self.config.getProperty('canonicalHost', '')
        if host:
            scheme = 'https' if useHTTPS else 'http'
            retval = '{scheme}://{host}'.format(scheme=scheme, host=host)
        elif self.siteObj:
            # --=mpj17=-- Things can get weird.
            retval = '/%s' % self.siteObj.absolute_url(1)
        else:
            # --=mpj17=-- Things can get very weird
            retval = '/'

        defaultPort = '443' if useHTTPS else '80'
        port = self.get_option('canonicalPort', defaultPort)
        if (((port != '443') and useHTTPS)  # Not using HTTPS on the default port
                or (port != '80') and (not useHTTPS)):  # Not using HTTP on the default port
            retval = '{0}:{1}'.format(retval, port)
        assert retval
        return retval

    @property
    def site_admins(self):
        return self.get_site_admins()

    def get_site_admins(self):
        admins = self.siteObj.users_with_local_role('DivisionAdmin')
        retval = [createObject('groupserver.UserFromId',
                  self.context, a) for a in admins]
        return retval

    @property
    def showImage(self):
        return self.config.getProperty('showImage', False)

    @property
    def skin(self):
        return self.config.getProperty('skin', 'green')

    def get_path(self):
        retval = '/'.join(self.siteObj.getPhysicalPath())
        assert len(retval) >= 1
        return retval

    def get_support_email(self):
        retval = XWFUtils.get_support_email(self.context, self.get_id())
        assert type(retval) == str
        assert retval
        assert '@' in retval
        return retval

    def get_property(self, prop, default=None):
        if self.siteObj is None:
            m = 'Site instance does not exist:\n  Context {0}\n  ID {1}'
            msg = m.format(self.context, self.id)
            raise ValueError(msg)
        retval = self.siteObj.getProperty(prop, default)
        if isinstance(retval, str):
            retval = to_unicode_or_bust(retval)
        return retval


class GSContentView(BrowserView):
    '''View object for standard GroupServer content objects'''
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.__siteInfo = self.__groupsInfo = None

    @property
    def siteInfo(self):
        if self.__siteInfo is None:
            self.__siteInfo = createObject('groupserver.SiteInfo',
                                           self.context)
        assert self.__siteInfo
        return self.__siteInfo

    @property
    def groupsInfo(self):
        if self.__groupsInfo is None:
            self.__groupsInfo = createObject(
                'groupserver.GroupsInfo', self.context)
        assert self.__groupsInfo
        return self.__groupsInfo

    def process_form(self):
        form = self.context.REQUEST.form
        result = {}
        if 'submitted' in form:
            submit = form.get('__submit__')
            model, instance = submit.split('+')
            model = form.get('model_override', model)

            site_root = self.context.site_root()

            localScripts = getattr(site_root.LocalScripts, 'forms', None)
            oldScripts = getattr(site_root.Scripts, 'forms')
            assert oldScripts, 'Could not get folder Scripts/forms'

            modelDir = (localScripts
                        and getattr(localScripts, model,
                                    getattr(oldScripts, model, None))
                        or getattr(oldScripts, model, None))
            if modelDir:
                assert hasattr(modelDir, model)
                if hasattr(modelDir, instance):
                    script = getattr(modelDir, instance)
                    assert script
                    retval = script()
                    return retval
                else:
                    m = """<p>Could not find the instance
                           <code>%s</code> in the model
                           <code>%s</code>.</p>""" % (instance, model)
                    result['error'] = True
                    result['message'] = m
            else:
                m = """<p>Could not find the model
                       <code>%s</code>.</p>""" % model
                result['error'] = True
                result['message'] = m
            assert 'error' in result
            assert 'message' in result
            assert result['message'].split

        result['form'] = form
        return result

    # To be converted: Scripts.get_firstLevelFolder(context)

InitializeClass(GSContentView)
