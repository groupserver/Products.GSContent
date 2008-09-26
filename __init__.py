# This space intentionally left blank
import groupsInfo, titleBar, view
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class

groupsInfo_security = ModuleSecurityInfo('Products.GSContent.groupsInfo')
from groupsInfo import GSGroupsInfoFactory, GSGroupsInfo
allow_class(GSGroupsInfoFactory)
allow_class(GSGroupsInfo)

groupsInfo_security = ModuleSecurityInfo('Products.GSContent.view')
from view import GSSiteInfo
allow_class(GSSiteInfo)

