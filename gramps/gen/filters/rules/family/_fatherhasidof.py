#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
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

# -------------------------------------------------------------------------
#
# Standard Python modules
#
# -------------------------------------------------------------------------
from ....const import GRAMPS_LOCALE as glocale

_ = glocale.translation.gettext

# -------------------------------------------------------------------------
#
# Gramps modules
#
# -------------------------------------------------------------------------
from .. import RegExpIdBase


# -------------------------------------------------------------------------
#
# Typing modules
#
# -------------------------------------------------------------------------
from gramps.gen.lib import Family
from gramps.gen.db import Database


# -------------------------------------------------------------------------
#
# HasNameOf
#
# -------------------------------------------------------------------------
class FatherHasIdOf(RegExpIdBase):
    """Rule that checks for a person with a specific Gramps ID"""

    labels = [_("Person ID:")]
    name = _("Families having father with Id containing <text>")
    description = _("Matches families whose father has a specified " "Gramps ID")
    category = _("Father filters")

    def apply_to_one(self, db: Database, family: Family) -> bool:  # type: ignore[override]
        father_handle = family.father_handle
        if father_handle:
            father = db.get_person_from_handle(father_handle)
            return super().apply_to_one(db, father) if father else False
        return False
