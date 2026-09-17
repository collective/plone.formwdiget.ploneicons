from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from zope.component import getUtility


class IconSelectorModal(BrowserView):
    """Modal view for icon selection."""

    def icons(self):
        registry = getUtility(IRegistry)
        icons = [
            k.replace("plone.icon.", "")
            for k in registry.records
            if k.startswith("plone.icon.")
        ]
        icons.sort()
        return icons
