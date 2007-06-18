from zope.interface import implements
import zope.interface
from zope.component import adapts, provideAdapter
from zope.publisher.interfaces import IRequest
from interfaces import IGSSiteInfo, IGSGroupsInfo
from zope.app.folder.interfaces import IFolder
from zope.component.interfaces import IFactory

class GSGroupsInfoFactory(object):
    implements(IFactory)
    
    title = u'GroupServer Groups Info Factory'
    descripton = u'Create a new GroupServer groups information instance'
    
    def __call__(self, context):
        retval = GSGroupsInfo(context)
        return retval
        
    def getInterfaces(self):
        retval = implementedBy(GSGroupsInfo)
        assert retval
        return retval

class GSGroupsInfo(object):
    implements( IGSGroupsInfo )
    adapts(IFolder)
    
    def __init__(self, context):
    
        self.context=context
        self.siteInfo = IGSSiteInfo(context)
        self.groupsObj = self.__get_groups_object()
        
        self.__allGroups = None
        self.__visibleGroups = None
        
    def __get_groups_object(self):
        assert self.siteInfo
        assert self.siteInfo.siteObj
        
        assert hasattr(self.siteInfo.siteObj, 'groups'), \
          'Site "%s" has not "groups" instance within "Content"' % \
          self.siteInfo.get_name()
        groupsObj = getattr(self.siteInfo.siteObj, 'groups')
        
        assert groupsObj.getProperty('is_groups' , False), \
          'Groups instance for "%s" exists, but the "is_groups" property '\
          'is not True' % siteInfo.get_name()
        
        assert groupsObj
        return groupsObj

    def get_all_groups(self):
        assert self.groupsObj
        if self.__allGroups == None:
            folderTypes = ['Folder', 'Folder (Ordered)']
            allGroups = [g for g in self.groupsObj.objectValues(folderTypes)
                          if g.getProperty('is_group', False)]
            self.__allGroups = allGroups
            
        return self.__allGroups

    def get_visible_groups(self):
        if self.__visibleGroups == None:
            allGroups = self.get_all_groups()
            
            # Quite a simple process, really: itterate through all the groups,
            #   checking to see if the "messages" instance is visible.
            visibleGroups = []
            for group in allGroups:
                try:
                    group.messages.getId()
                except:
                    continue
                else:
                    visibleGroups.append(group)
            self.__visibleGroups = visibleGroups
        return self.__visibleGroups
        
    def get_visible_group_ids(self):
        retval = [g.getId() for g in self.get_visible_groups()]
        return retval

    def filter_visible_group_ids(self, gIds):
        visibleGroupIds = self.get_visible_group_ids()
        return [g for g in gIds if (g in visibleGroupIds)]

