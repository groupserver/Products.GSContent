# This space intentionally left blank
import titleBar, view
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class, allow_module

siteInfo_security = ModuleSecurityInfo('Products.GSContent.view')
from view import GSSiteInfo
allow_class(GSSiteInfo)

# XXX: Dirty hack, purely to support legacy code. Remove as soon as possible
def GSGroupsInfoFactory():
    logger.warn("Deprecated: GSGroupsInfoFactory should be imported directly fr$
    from gs.groups.groupsInfo import GSGroupsInfoFactory as GSGIFactory
    return GSGIFactory()

allow_module('Products.GSContent.GSGroupsInfoFactory')

