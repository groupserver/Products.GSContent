from zope.component import createObject
import zope.app.pagetemplate.viewpagetemplatefile
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
import zope.interface, zope.component, zope.publisher.interfaces
import zope.viewlet.interfaces, zope.contentprovider.interfaces 
from interfaces import *


class GSSiteImageContentProvider(object):
    """GroupServer view of the site image
    """

    zope.interface.implements( IGSSiteImage )
    zope.component.adapts(zope.interface.Interface,
        zope.publisher.interfaces.browser.IDefaultBrowserLayer,
        zope.interface.Interface)

    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.__updated = False

        self.context = context
        self.request = request
        
    def update(self):
        self.__updated = True

        self.siteInfo = createObject('groupserver.SiteInfo', 
          self.context)

    def render(self):
        if not self.__updated:
            raise interfaces.UpdateNotCalled

        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        return pageTemplate(view=self)
        
    #########################################
    # Non standard methods below this point #
    #########################################

    @property
    def siteName(self):
        retval = u''
        retval = self.siteInfo.get_name()
        return retval
        
    @property
    def siteImageUrl(self):
       siteId = self.siteInfo.get_id()
       retval = (hasattr(self.context, '%s.jpg' % siteId) and '%s.jpg' % siteId) or 
          (hasattr(self.context, '%s.png' % siteId) and '%s.png' % siteId) or
          (hasattr(self.context, '%s.gif' % siteId) and '%s.gif' % siteId) or ''
        assert type(retval) == str
        return retval
        
    @property
    def siteImageShow(self):
        retval = self.showImageRegardlessOfSiteSetting or \
          getattr(self.siteInfo, 'showImage', False)
        assert type(retval) == bool
        return retval

    @property
    def siteTextShow(self):
        retval = self.showImageWithSiteName
        assert type(retval) == bool
        return retval

zope.component.provideAdapter(GSSiteImageContentProvider,
    provides=zope.contentprovider.interfaces.IContentProvider,
    name="groupserver.titleBar")

