from zope.component import createObject, adapts, provideAdapter
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.interface import implements, Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.contentprovider.interfaces import IContentProvider, UpdateNotCalled

from interfaces import IGSSiteImage

class GSSiteImageContentProvider(object):
    """GroupServer view of the site image
    """

    implements( IGSSiteImage )
    adapts(Interface, IDefaultBrowserLayer, Interface)

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
            raise UpdateNotCalled

        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        return pageTemplate(view=self)
        
    #########################################
    # Non standard methods below this point #
    #########################################

    @property
    def siteName(self):
        retval = self.siteInfo.get_name()
        return retval
        
    @property
    def siteImageUrl(self):
        exts = ['png', 'jpg', 'gif']
        imgs = [i for i in [self.__imgName(ext) for ext in exts] if i]
        if imgs:
            retval = imgs[0]
        else:
            retval = ''
        assert type(retval) == str
        return retval

    def __imgName(self, ext):
        imgName = '%s.%s' % (self.siteInfo.id, ext)
        retval = hasattr(self.context, imgName) and imgName or ''
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

provideAdapter(GSSiteImageContentProvider,
               provides=IContentProvider,
               name="groupserver.TitleBar")

