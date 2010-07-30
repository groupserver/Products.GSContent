# This space intentionally left blank
import titleBar, view
from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class

siteInfo_security = ModuleSecurityInfo('Products.GSContent.view')
from view import GSSiteInfo
allow_class(GSSiteInfo)

