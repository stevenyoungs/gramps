#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2008  Brian G. Matherly
# Copyright (C) 2008  Jerome Rapinat
# Copyright (C) 2008  Benny Malengier
# Copyright (C) 2010  Gary Burton - derived from _HasGalleryBase.py
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
# gen.filters.rules/Source/_HasRepository.py

# -------------------------------------------------------------------------
#
# Standard Python modules
#
# -------------------------------------------------------------------------
from ....const import GRAMPS_LOCALE as glocale

# -------------------------------------------------------------------------
#
# Gramps modules
#
# -------------------------------------------------------------------------
from .. import Rule


# -------------------------------------------------------------------------
#
# Typing modules
#
# -------------------------------------------------------------------------
from ....lib import Source
from ....db import Database


_ = glocale.translation.gettext


# -------------------------------------------------------------------------
# "People who have images"
# -------------------------------------------------------------------------
class HasRepository(Rule):
    """Objects which reference repositories"""

    labels = [_("Number of instances:"), _("Number must be:")]
    name = _("Sources with <count> Repository references")
    description = _("Matches sources with a certain number of repository references")
    category = _("General filters")

    def prepare(self, db: Database, user):
        # things we want to do just once, not for every handle
        if self.list[1] == "less than":
            self.count_type = 0
        elif self.list[1] == "greater than":
            self.count_type = 2
        else:
            self.count_type = 1  # "equal to"

        self.userSelectedCount = int(self.list[0])

    def apply_to_one(self, db, obj: Source) -> bool:
        count = len(obj.reporef_list)
        if self.count_type == 0:  # "less than"
            return count < self.userSelectedCount
        elif self.count_type == 2:  # "greater than"
            return count > self.userSelectedCount
        # "equal to"
        return count == self.userSelectedCount
