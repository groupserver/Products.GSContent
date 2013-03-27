# This space intentionally left blank
import view
from AccessControl import ModuleSecurityInfo, allow_class, allow_module
from Products.GSContent.view import GSSiteInfo

siteInfo_security = ModuleSecurityInfo('Products.GSContent.view')
allow_class(GSSiteInfo)

# XXX: Dirty hack, purely to support legacy code. Remove as soon as possible
def GSGroupsInfoFactory():
    import logging
    logger = logging.getLogger("Products.GSContent")
    logger.warn("Deprecated: GSGroupsInfoFactory should be imported directly "
                "from gs.groups.groupsInfo")
    from gs.groups.groupsInfo import GSGroupsInfoFactory as GSGIFactory
    return GSGIFactory()

allow_module('Products.GSContent.GSGroupsInfoFactory')

