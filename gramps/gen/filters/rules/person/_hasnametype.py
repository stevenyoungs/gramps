#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2010  Gramps
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""
Rule that checks the type of name.
"""

# -------------------------------------------------------------------------
#
# Gramps modules
#
# -------------------------------------------------------------------------
from ....const import GRAMPS_LOCALE as glocale
from ....lib.nametype import NameType
from .. import Rule

_ = glocale.translation.gettext


# -------------------------------------------------------------------------
#
# Typing modules
#
# -------------------------------------------------------------------------
from gramps.gen.lib import Person
from gramps.gen.db import Database


# -------------------------------------------------------------------------
#
# HasNameType
#
# -------------------------------------------------------------------------
class HasNameType(Rule):
    """
    Rule that checks the type of name.
    """

    labels = [_("Name type:")]
    name = _("People with the <Name type>")
    description = _("Matches people with a type of name")
    category = _("General filters")

    def __init__(self, arg, use_regex=False, use_case=False):
        super().__init__(arg, use_regex, use_case)
        self.name_type = None

    def prepare(self, db, user):
        """
        Prepare the rule. Things we only want to do once.
        """
        if self.list[0]:
            self.name_type = NameType()
            self.name_type.set_from_xml_str(self.list[0])

    def apply(self, _db, obj):
        """
        Apply the rule. Return True on a match.
        """
        if self.name_type:
            for name in [obj.get_primary_name()] + obj.get_alternate_names():
                if name.get_type() == self.name_type:
                    return True
        return False
