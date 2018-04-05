# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import provider


_ = MessageFactory('collective.translation_folder')


@provider(IFormFieldProvider)
class ITranslationFolder(model.Schema):

    model.fieldset('settings', label=_(u'Settings'),
                   fields=['contains_translations'])

    contains_translations = schema.Bool(
        title=_(
            u'help_contains_translations',
            default=u'Contains translations'),
        description=_(
            u'help_contains_translations_description',
            default=u'If selected, marks this folder as containing '
                    u'multiple translations of the same content.'),
        default=False,
        required=False,
    )
