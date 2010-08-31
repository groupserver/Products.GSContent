# This space intentionally left blank
import titleBar, view
import logging
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class, allow_module

logger = logging.getLogger("Products.GSContent")

from Products.GSContent.view import GSSiteInfo

siteInfo_security = ModuleSecurityInfo('Products.GSContent.view')
allow_class(GSSiteInfo)

# XXX: Dirty hack, purely to support legacy code. Remove as soon as possible
def GSGroupsInfoFactory():
    logger.warn("Deprecated: GSGroupsInfoFactory should be imported directly "
                "from gs.groups.groupsInfo")
    from gs.groups.groupsInfo import GSGroupsInfoFactory as GSGIFactory
    return GSGIFactory()

allow_module('Products.GSContent.GSGroupsInfoFactory')

