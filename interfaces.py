from zope.interface.interface import Interface
from zope.contentprovider.interfaces import IContentProvider
from zope.schema import *

class IFolder(Interface):
    pass

class IGSContentFolder(Interface):
    pass

class IGSFullPageContentFolder(Interface):
    pass

class IGSSiteFolder(Interface):
    pass

class IGSSiteHomepageFolder(IGSSiteFolder):
    pass

class IGSNotificationPreview(Interface):
    pass

class IGSNotficationPreview(Interface): # TODO: delete
    pass

class IGSSiteInfo(Interface):
    pass


class IGSGroupInfo(Interface):
    def get_id():
        """Get the ID of the group"""
    def get_name():
        """Get the name of the group"""
    def get_url():
        """Get the URL of the group"""

class IGSGroupsInfo(Interface):
    def get_visible_group_ids():
        """Get the IDs of Visible Groups
        
        ARGUMENTS
            None.
            
        RETURNS
            A list of strings, representing the IDs of visible groups.
        """

class IGSTitleBar(IContentProvider):
    """Render the site title bar, with image and/or sitename"""
    
    pageTemplateFileName = Text(title=u"Page Template File Name",
      description=u'The name of the ZPT file that is used to render the '\
        u'site image.',
      required=False,
      default=u"browser/templates/siteImage.pt")
       
    showImageRegardlessOfSiteSetting = Bool(
      title=u'Show Image Regardless of Site Setting',
      description=u"Show the site image, regardless of the value of "
        u"the showImage property.",
      required=False,
      default=False)
      
    showImageWithSiteName = Bool(
      title=u'Show Image With the Site Name',
      description=u"Show the site image with the site name text.",
      required=False,
      default=True)

