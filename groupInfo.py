import zope.interface
from interfaces import IGSSiteInfo, IGSGroupInfo

class GSGroupInfo(object):
    zope.interface.implements( IGSGroupInfo )
    
    def __init__(self, context, groupId=None):
        self.context=context
        self.groupId = groupId
        self.siteInfo = IGSSiteInfo(context)
        self.groupObj = self.__get_group_object()
        
    def __get_group_object(self):
        retval = None
        if self.groupId:
            retval = self.__get_group_object_by_id(self.groupId)
        else:
            retval = self.__get_group_object_by_acquisition()
        return retval
        
    def __get_group_object_by_id(self, groupId):
        retval = None
        
        site_root = self.context.site_root()
        content = getattr(site_root, 'Content')
        site = getattr(content, self.siteInfo.get_id())
        groups = getattr(site, 'groups')
        
        if hasattr(groups, groupId):
            retval = getattr(groups, groupId)
            
        return retval
        
    def __get_group_object_by_acquisition(self):
        """Get the group object by acquisition
        
        Walk back up the location-hierarchy looking for the group object,
        which is marked by the "is_group" attribute (set to True). For the
        most part, the code was taken from 
          "GroupServer/Scripts/get/group_object.py"
        
        Returns
          None, if no group can be found, or the Folder object if a 
          group is found.
        """
        retval = None
        
        group_object = self.context
        while group_object:
            try:
                group_object = group_object.aq_parent
                if getattr(group_object.aq_inner.aq_explicit, 'is_group', 0):
                    break
            except:
                break
        try:
            if getattr(group_object.aq_inner.aq_explicit, 'is_group', 0):
                retval = group_object.aq_inner.aq_explicit
        except:
            pass
        return retval
        
    def group_exists(self):
        return (self.groupObj != None)

    def get_id(self):
        retval = ''
        if self.group_exists():
            retval = self.groupObj.getId()
        return retval
        
    def get_name(self):
        retval = ''
        if self.group_exists():
            retval = self.groupObj.title_or_id()
        return retval

    def get_url(self):
        retval = '%s/groups' % self.siteInfo.get_url()
        if self.group_exists():
            retval = '%s/%s' % (retval, self.getId)
        return retval

