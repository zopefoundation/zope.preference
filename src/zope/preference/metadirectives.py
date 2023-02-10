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
"""``apidoc:preferencesgroup`` ZCML directive interface

"""
from zope.configuration import fields
from zope.interface import Interface
from zope.schema import DottedName


class OptionalDottedName(DottedName):

    def _validate(self, value):
        if value:
            super()._validate(value)


class IPreferenceGroupDirective(Interface):
    """Register a preference group."""

    # The id is not required, since the root group has an empty id.
    id = OptionalDottedName(
        title="Id",
        description="""
            Id of the preference group used to access the group. The id should
            be a valid path in the preferences tree.""",
        required=False,
    )

    schema = fields.GlobalInterface(
        title="Schema",
        description="Schema of the preference group used defining the "
                    "preferences of the group.",
        required=False
    )

    title = fields.MessageID(
        title="Title",
        description="Title of the preference group used in UIs.",
        required=True
    )

    description = fields.MessageID(
        title="Description",
        description="Description of the preference group used in UIs.",
        required=False
    )

    category = fields.Bool(
        title="Is Group a Category",
        description="Denotes whether this preferences group is a category.",
        required=False,
        default=False
    )
