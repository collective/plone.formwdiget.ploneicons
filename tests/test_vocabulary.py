from plone.registry import field
from plone.registry import Record
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import pytest


def test_vocabulary_registration(portal):
    factory = getUtility(IVocabularyFactory, name="plone.formwidget.ploneicons.Icons")
    assert factory is not None


def test_vocabulary_values(portal):
    registry = getUtility(IRegistry)
    # Mock some icons in the registry
    if "plone.icon.alarm" not in registry:
        registry.records["plone.icon.alarm"] = Record(
            field.TextLine(title="Alarm"), "alarm.svg"
        )
    if "plone.icon.home" not in registry:
        registry.records["plone.icon.home"] = Record(
            field.TextLine(title="Home"), "home.svg"
        )

    factory = getUtility(IVocabularyFactory, name="plone.formwidget.ploneicons.Icons")
    vocabulary = factory(portal)
    # Should contain at least our mocked icons (short names)
    values = [term.value for term in vocabulary]
    assert "alarm" in values
    assert "home" in values
    # Should not contain the prefix
    for val in values:
        assert not val.startswith("plone.icon.")


def test_vocabulary_sorting(portal):
    registry = getUtility(IRegistry)
    if "plone.icon.alarm" not in registry:
        registry.records["plone.icon.alarm"] = Record(
            field.TextLine(title="Alarm"), "alarm.svg"
        )
    if "plone.icon.home" not in registry:
        registry.records["plone.icon.home"] = Record(
            field.TextLine(title="Home"), "home.svg"
        )
    if "plone.icon.user" not in registry:
        registry.records["plone.icon.user"] = Record(
            field.TextLine(title="User"), "user.svg"
        )

    factory = getUtility(IVocabularyFactory, name="plone.formwidget.ploneicons.Icons")
    vocabulary = factory(portal)
    values = [term.value for term in vocabulary]
    # Filter to our known ones for sorting check
    test_values = [v for v in values if v in ("alarm", "home", "user")]
    assert test_values == ["alarm", "home", "user"]
