"""Module where all interfaces, events and exceptions live."""

from z3c.form.interfaces import ITextWidget
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPloneIconsWidget(ITextWidget):
    """Marker interface for the Plone Icons widget."""
