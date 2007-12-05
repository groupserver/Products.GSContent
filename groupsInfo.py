from zope.interface import implements
import zope.interface
from zope.component import adapts, provideAdapter
from zope.publisher.interfaces import IRequest
from interfaces import IGSSiteInfo, IGSGroupsInfo
from zope.app.folder.interfaces import IFolder
from zope.component.interfaces import IFactory

import AccessControl
from Products.GSGroup.queries import GroupQuery

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
        self.folderTypes = ['Folder', 'Folder (Ordered)']

        self.da = context.zsqlalchemy
        self.groupQuery = GroupQuery(context, self.da)
        
    def __get_groups_object(self):
        assert self.siteInfo, 'Site Info is set to %s' % self.siteInfo
        assert self.siteInfo.siteObj, \
          'Site Object is %s' % self.siteInfo.siteObj
        
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
            allGroups = [g for g in \
                         self.groupsObj.objectValues(self.folderTypes)
                         if g.getProperty('is_group', False)]
            self.__allGroups = allGroups
            
        return self.__allGroups

    def get_visible_groups(self):
        if self.__visibleGroups == None:
            securityManager = AccessControl.getSecurityManager()

            allGroups = self.get_all_groups()
            
            # Quite a simple process, really: itterate through all the groups,
            #   checking to see if the "messages" instance is visible.
            visibleGroups = []
            for group in allGroups:
                if (hasattr(group, 'messages')
                  and securityManager.checkPermission('View', group)
                  and securityManager.checkPermission('View', group.aq_explicit.messages)):
                    visibleGroups.append(group)
            self.__visibleGroups = visibleGroups
        return self.__visibleGroups
        
    def get_visible_group_ids(self):
        retval = [g.getId() for g in self.get_visible_groups()]
        return retval

    def filter_visible_group_ids(self, gIds):
        visibleGroupIds = self.get_visible_group_ids()
        return [g for g in gIds if (g in visibleGroupIds)]

    def get_member_groups_for_user(self, user, authenticatedUser):
        """Get a list of all groups that the user is a member of.
        
        ARGUMENTS
            user: A user instance to query.
            authenticatedUser: The instance of the user who is requesting 
                the information.
        
        RETURNS
            A list of groups the user is a member of. If "user" is the
            same as the "authenticatedUser", then the list will be of all
            groups that "user" is a member of. Otherwise only the groups
            that the user is a member of, and has posted to, will be 
            listed.
        
        SIDE EFFECTS
            None.
        """
        assert user
        retval = []
        if (user.getId() == authenticatedUser.getId()):
            retval = self.__get_member_groups_for_user(user)
        else:
            retval = self.__get_visible_member_groups_for_user(user)
        assert type(retval) == list
        return retval

    def __get_member_groups_for_user(self, user):
        """Get a list of all groups the user is currently a member of.
        
        WARNING
            Showing group-memberships to the wrong people may result in
            a privacy breach. It is safer to use 
            "get_member_groups_for_user"
            
        ARGUMENTS
            user: A user instance.
            
        RETURNS
            A list of all groups the user is currently a member of.
        
        SIDE EFFECTS
            None.
        """
        assert user
        visibleGroups = self.get_visible_groups()
        retval = [g for g in visibleGroups
                  if 'GroupMember' in user.getRolesInContext(g)]
        assert type(retval) == list
        return retval

    def __get_visible_member_groups_for_user(self, user):
        """Get the publicly visible groups that the user is a member of.
        
        ARGUMENTS
            user: A user instance.
            
        RETURNS
            A list of groups that the user is currently a member of, and
            has posted to.
        
        SIDE EFFECTS
            None.
        """
        assert user
        retval = []
        memberGroups = self.__get_member_groups_for_user(user)
        sId = self.siteInfo.get_id()
        uId = user.getId()
        q = self.groupQuery
        for g in memberGroups:
            authors = [ar['user_id'] for ar in
                        q.authors_posts_in_group(sId, g.getId())]
            if uId in authors:
                retval.append(g)
        assert type(retval) == list
        return retval

