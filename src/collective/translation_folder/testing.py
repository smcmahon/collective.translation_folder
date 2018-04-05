# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.translation_folder


class CollectiveTranslationFolderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.translation_folder)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.translation_folder:default')


COLLECTIVE_TRANSLATION_FOLDER_FIXTURE = CollectiveTranslationFolderLayer()


COLLECTIVE_TRANSLATION_FOLDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TRANSLATION_FOLDER_FIXTURE,),
    name='CollectiveTranslationFolderLayer:IntegrationTesting'
)


COLLECTIVE_TRANSLATION_FOLDER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TRANSLATION_FOLDER_FIXTURE,),
    name='CollectiveTranslationFolderLayer:FunctionalTesting'
)


COLLECTIVE_TRANSLATION_FOLDER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_TRANSLATION_FOLDER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveTranslationFolderLayer:AcceptanceTesting'
)
