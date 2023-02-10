##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for the Preferences System
"""
import doctest
import unittest

import zope.component.hooks
import zope.component.testing
import zope.testing.module
from zope.interface.verify import verifyObject
from zope.testing import cleanup

from zope import component
from zope.preference.interfaces import IPreferenceGroup


def addUtility(sitemanager, utility, iface=None, name='', suffix=''):
    folder_name = (name or (iface.__name__ + 'Utility')) + suffix
    default = sitemanager['default']
    default[folder_name] = utility
    utility = default[folder_name]
    sitemanager.registerUtility(utility, iface, name)
    return utility


def setUp(test):
    zope.component.testing.setUp(test)
    zope.component.hooks.setHooks()

    # Traversal
    from zope.container.interfaces import ISimpleReadContainer
    from zope.container.traversal import ContainerTraversable
    from zope.traversing.interfaces import ITraversable
    from zope.traversing.testing import setUp as traversalSetUp
    traversalSetUp()
    zope.component.provideAdapter(ContainerTraversable,
                                  (ISimpleReadContainer,), ITraversable)

    # ISiteManager lookup
    from zope.interface import Interface
    from zope.interface.interfaces import IComponentLookup
    from zope.site.site import SiteManagerAdapter
    zope.component.provideAdapter(SiteManagerAdapter, (Interface,),
                                  IComponentLookup)

    # Creating a root folder and making it current is
    # done in the doctest.

    test.globs['addUtility'] = addUtility
    zope.testing.module.setUp(test, 'zope.preference.README')


def tearDown(test):
    zope.component.testing.tearDown(test)
    zope.testing.module.tearDown(test)


class TestConfiguration(cleanup.CleanUp,
                        unittest.TestCase):

    def test_configure(self):
        from zope.configuration import xmlconfig

        from zope.preference.default import DefaultPreferenceGroup
        from zope.preference.default import DefaultPreferenceProvider

        xmlconfig.string("""
        <configure xmlns="http://namespaces.zope.org/zope">
            <include package="zope.preference" />
        </configure>
        """)

        # We have a default utility
        utility = component.getUtility(IPreferenceGroup)
        verifyObject(IPreferenceGroup, utility)

        # We can adapt preference providers
        provider = DefaultPreferenceProvider()
        prefs = component.getMultiAdapter((provider, None), name="preferences")
        self.assertIsInstance(prefs, DefaultPreferenceGroup)


def test_suite():
    readme = doctest.DocFileSuite(
        'README.rst',
        setUp=setUp, tearDown=tearDown,
        optionflags=(doctest.NORMALIZE_WHITESPACE
                     | doctest.ELLIPSIS
                     | doctest.IGNORE_EXCEPTION_DETAIL))
    return unittest.TestSuite((
        readme,
        unittest.defaultTestLoader.loadTestsFromName(__name__),
    ))
