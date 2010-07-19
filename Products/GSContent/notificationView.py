# coding=utf-8
'''GroupServer-Content View Class
'''
from App.class_init import InitializeClass
from Products.Five import BrowserView
from zope.component import createObject

from Products.XWFCore import XWFUtils

class GSNotificationView(BrowserView):
    '''View object for standard GroupServer content objects'''
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.siteInfo = createObject('groupserver.SiteInfo', context)
        
    def __get_n_dict(self):
        loggedInUser = self.request.AUTHENTICATED_USER
        user = self.context.acl_users.getUserById(loggedInUser.getId())

        n_dict = {
            'siteName': self.siteInfo.get_name(),
            'siteId': self.siteInfo.get_id(),
            'canonicalHost': self.siteInfo.get_url().strip('http://'),
            'canonical': self.siteInfo.get_url().strip('http://'),
            'supportEmail': self.siteInfo.get_support_email(),
            # Get User Stuff
            'preferredName': XWFUtils.get_user_realnames(user),
            'mailto': user.get_emailAddresses()[0],
        }
        for propertyId in self.context.propertyIds():
            n_dict[propertyId] = self.context.getProperty(propertyId)
            
        return n_dict
        
    def __call__(self):
        n_type = self.context.getId()
        n_id = 'default'
        n_dict = self.__get_n_dict()
        loggedInUser = self.request.AUTHENTICATED_USER
        user = self.context.acl_users.getUserById(loggedInUser.getId())
        email = user.get_emailAddresses()[0]
        retval = user.render_notification(n_type, n_id, n_dict, email)
        
        return retval
                
InitializeClass( GSNotificationView )

