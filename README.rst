=============================
collective.translation_folder
=============================

plone.app.multilingual is what you want if you're translating a whole site.
If you're only translating a portion of the content, this package may help organize it and present it to users.


Features
--------

The scheme is that you mark a folder as containing multiple translations of the same content item.
That option appears on the ``settings`` tab of eligible folderish items.
One of those content items will probably be the default content item for the folder, and it will probably be in your site's default language.
Translated content items should have their language set in the ``categorization`` tab.

Now, when one of the translated content items (including the default) is displayed, a viewlet above the title will provide links to all of the alternative translations.

When a translation folder is inside another folder, if you use the ``summary`` listing, the listing for the translation folder will include links to the alternative translations.



Installation
------------

This package only works with Plone 5.1.
If it's successful, we'll keep git branches for various Plone versions.

Install collective.translation_folder by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.translation_folder


and then running ``bin/buildout``

Use the "Add ons" site setup configlet to add it to a site.

Then, go to the "Dexterity content types" configlet and add it as a behavior to any folderish Dexterity content type for which you want to offer this option.
That may be just the ``folder`` content type.


Contribute
----------

- Issue Tracker: https://github.com/smcmahon/collective.translation_folder/issues
- Source Code: https://github.com/smcmahon/collective.translation_folder


Support
-------

If you are having issues, leave a message on the Plone community board.


License
-------

The project is licensed under the GPLv2.
