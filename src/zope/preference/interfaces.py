##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
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
"""User Preferences Interfaces
"""
__docformat__ = "reStructuredText"

import zope.interface
import zope.schema
from zope.configuration.fields import MessageID
from zope.location.interfaces import ILocation


class IPreferenceGroup(ILocation):
    """A group of preferences.

    This component represents a logical group of preferences. The preferences
    contained by this group is defined through the schema. The group has also
    a name by which it can be accessed.

    The fields specified in the schema *must* be available as attributes and
    items of the group instance. It is up to the implementation how this is
    realized, however, most often one will implement __setattr__ and
    __getattr__ as well as the common mapping API.

    The reason all the API fields are doubly underlined is to avoid name
    clashes.
    """

    __id__ = zope.schema.TextLine(
        title="Id",
        description="The id of the group.",
        required=True)

    __schema__ = zope.schema.InterfaceField(
        title="Schema",
        description="Schema describing the preferences of the group.",
        required=False)

    __title__ = MessageID(
        title="Title",
        description="The title of the group used in the UI.",
        required=True)

    __description__ = MessageID(
        title="Description",
        description="The description of the group used in the UI.",
        required=False)


class IPreferenceCategory(zope.interface.Interface):
    """A collection of preference groups.

    Objects providing this interface serve as groups of preference
    groups. This allows UIs to distinguish between high- and low-level
    prefernce groups.
    """


class IUserPreferences(zope.interface.Interface):
    """Objects providing this interface have to provide the root preference
    group API as well."""


class IDefaultPreferenceProvider(zope.interface.Interface):
    """A root object providing default values for the entire preferences tree.

    Default preference providers are responsible for providing default values
    for all preferences. The way they get these values are up to the
    implementation.
    """

    preferences = zope.schema.Field(
        title="Default Preferences Root",
        description="Link to the default preferences")
