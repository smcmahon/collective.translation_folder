# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.defaultpage import get_default_page
from Products.Five import BrowserView
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.translation_folder')


class TranslationsAvailableView(BrowserView):
    """ Show available translations for this content
    """

    def translations_available_text(self):
        return _(u'Translations available:')

    def site_language(self):
        return api.portal.get_default_language()

    def item_language(self, item):
        return item.Language() or self.site_language()

    def item_children(self, obj):
        """ find translations among children of obj.
            Criteria:
                * not default page
                * not excluded from nav
                * not in the language of the default page, folder, site
        """

        def cmp_lang(a, b):
            return cmp(a['lang_name'], b['lang_name'])

        pl = api.portal.get_tool(name='portal_languages')
        languages = pl.getAvailableLanguages()
        site_language_info = languages.get(self.site_language())

        results = api.content.find(context=obj)
        my_id = obj.id
        base_lang = None
        default_page_id = get_default_page(obj)
        if default_page_id is not None:
            default_page = obj.get(default_page_id)
            if default_page is not None:
                base_lang = self.item_language(default_page)
        if base_lang is None:
            base_lang = self.item_language(obj)
        results = [
            r for r in results
            if r.id not in (my_id, default_page_id) and not r.exclude_from_nav
        ]
        rez = []
        for r in results:
            ro = r.getObject()
            item_language = self.item_language(ro)
            lang_info = languages.get(item_language, site_language_info)
            if item_language != base_lang:
                rez.append(dict(
                    lang=item_language,
                    url=ro.absolute_url(),
                    lang_name=lang_info[u'name'],
                    lang_native=lang_info[u'native'],
                ))
        return sorted(rez, cmp_lang)
