# This space intentionally left blank
import groupsInfo, groupInfo, titleBar, view
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class

module_security = ModuleSecurityInfo('Products.GSContent')
groupInfo_security = ModuleSecurityInfo('Products.GSContent.groupInfo')
from groupInfo import GSGroupInfoFactory, GSGroupInfo
allow_class(GSGroupInfoFactory)
allow_class(GSGroupInfo)

groupsInfo_security = ModuleSecurityInfo('Products.GSContent.groupsInfo')
from groupsInfo import GSGroupsInfoFactory, GSGroupsInfo
allow_class(GSGroupsInfoFactory)
allow_class(GSGroupsInfo)

groupsInfo_security = ModuleSecurityInfo('Products.GSContent.view')
from view import GSSiteInfo
allow_class(GSSiteInfo)

