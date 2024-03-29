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
"""This module handles the 'preference' namespace directives.

"""
__docformat__ = 'restructuredtext'

from zope.component.zcml import utility

from zope.preference.interfaces import IPreferenceGroup
from zope.preference.preference import PreferenceGroup


def preferenceGroup(_context, id=None, schema=None,
                    title='', description='', category=False):
    if id is None:
        id = ''
    group = PreferenceGroup(id, schema, title, description, category)
    utility(_context, IPreferenceGroup, group, name=id)
