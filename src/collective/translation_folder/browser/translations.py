# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.defaultpage import get_default_page
from Products.Five import BrowserView


class TranslationsAvailableView(BrowserView):
    """ Show available translations for this content
    """

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
        default_page = get_default_page(obj)
        if default_page is not None:
            default_page_id = default_page.id
            base_lang = self.item_language(default_page)
        else:
            default_page_id = None
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
