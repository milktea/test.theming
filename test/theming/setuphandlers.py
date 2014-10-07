from collective.grok import gs
from test.theming import MessageFactory as _

@gs.importstep(
    name=u'test.theming', 
    title=_('test.theming import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('test.theming.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
