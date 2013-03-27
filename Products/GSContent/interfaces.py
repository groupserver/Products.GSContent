from zope.interface.interface import Interface
from zope.schema import Bool, Text

class IFolder(Interface):
    pass

class IGSContentFolder(Interface):
    pass

class IGSFullPageContentFolder(Interface):
    pass

class IGSSiteFolder(Interface):
    pass

class IGSNotificationPreview(Interface):
    pass

class IGSNotficationPreview(Interface): # TODO: delete
    pass

class IGSSiteInfo(Interface):
    pass
