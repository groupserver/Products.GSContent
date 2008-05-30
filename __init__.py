# This space intentionally left blank
import groupsInfo, groupInfo, titleBar
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class
module_security = ModuleSecurityInfo('Products.GSContent')
groupInfo_security = ModuleSecurityInfo('Products.GSContent.groupInfo')
from groupInfo import GSGroupInfoFactory
allow_class(GSGroupInfoFactory)

groupsInfo_security = ModuleSecurityInfo('Products.GSContent.groupsInfo')
from groupsInfo import GSGroupsInfoFactory, GSGroupsInfo
allow_class(GSGroupsInfoFactory)
allow_class(GSGroupsInfo)


