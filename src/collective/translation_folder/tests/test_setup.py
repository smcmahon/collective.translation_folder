# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.translation_folder.testing import COLLECTIVE_TRANSLATION_FOLDER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.translation_folder is properly installed."""

    layer = COLLECTIVE_TRANSLATION_FOLDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.translation_folder is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.translation_folder'))

    def test_browserlayer(self):
        """Test that ICollectiveTranslationFolderLayer is registered."""
        from collective.translation_folder.interfaces import (
            ICollectiveTranslationFolderLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveTranslationFolderLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TRANSLATION_FOLDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.translation_folder'])

    def test_product_uninstalled(self):
        """Test if collective.translation_folder is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.translation_folder'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTranslationFolderLayer is removed."""
        from collective.translation_folder.interfaces import \
            ICollectiveTranslationFolderLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveTranslationFolderLayer,
           utils.registered_layers())
