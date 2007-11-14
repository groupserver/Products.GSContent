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


