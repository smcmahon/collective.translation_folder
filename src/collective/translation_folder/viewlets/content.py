# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import common as base
from zope.i18nmessageid import MessageFactory

import Acquisition

_ = MessageFactory('collective.translation_folder')


class TranslationsAvailableViewlet(base.ViewletBase):
    """ Show available translations for this content
    """

    def translations_available_text(self):
        return _(u'Translations are available for this document:')

    def my_type(self):
        """ what's my portal type?
        """

        return Acquisition.aq_base(self.context).portal_type

    def site_language(self):
        return api.portal.get_default_language()

    def item_language(self, item):
        return item.Language() or self.site_language()

    def my_language(self):
        return self.item_language(Acquisition.aq_inner(self.context))

    def my_siblings(self):
        """ find siblings with the same portal_type.
        """

        context = Acquisition.aq_base(self.context)
        parent = Acquisition.aq_parent(self.context)
        portal_type = context.portal_type
        my_id = context.id
        sibs = api.content.find(context=parent, portal_type=portal_type, depth=1)
        return [s for s in sibs if s.id != my_id]

    def translations_available(self):

        def cmp_lang(a, b):
            return cmp(a['lang_name'], b['lang_name'])

        pl = api.portal.get_tool(name='portal_languages')
        languages = pl.getAvailableLanguages()
        sibs = [sib.getObject() for sib in self.my_siblings()]
        my_language = self.my_language()
        rez = []
        for sib in sibs:
            sib_language = self.item_language(sib)
            lang_info = languages.get(sib_language, languages.get(self.site_language()))
            if my_language != sib_language:
                rez.append(dict(
                    title=sib.Title(),
                    lang_code=sib_language,
                    lang_name=lang_info[u'name'],
                    lang_native=lang_info[u'native'],
                    url=sib.absolute_url(),
                ))
        return sorted(rez, cmp_lang)

    def render(self):
        """ render only if we're in a translatable folder
        """

        parent = Acquisition.aq_parent(self.context)
        if getattr(parent, 'contains_translations', False):
            # Call parent method which performs the actual rendering
            return self.index()
        else:
            # No output when the viewlet is disabled
            return ""
