from plone.app.z3cform.widgets.text import TextWidget
from plone.formwidget.ploneicons.interfaces import IPloneIconsWidget
from plone.registry.interfaces import IRegistry
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import implementer_only


@implementer_only(IPloneIconsWidget)
class PloneIconsWidget(TextWidget):
    """Plone Icons widget."""

    klass = "plone-icons-widget"

    def icons(self):
        registry = getUtility(IRegistry)
        icons = [
            k.replace("plone.icon.", "")
            for k in registry.records
            if k.startswith("plone.icon.")
        ]
        icons.sort()
        return icons

    def get_icon(self, icon_name):
        icon_view = getMultiAdapter((self.context, self.request), name="icon")
        return icon_view(name=icon_name)


@adapter(IPloneIconsWidget, IFormLayer)
@implementer(IFieldWidget)
def PloneIconsFieldWidget(field, request):
    return FieldWidget(field, PloneIconsWidget(request))
