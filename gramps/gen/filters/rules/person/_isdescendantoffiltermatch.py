#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2007  Donald N. Allingham
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
from ._isdescendantof import IsDescendantOf
from ._matchesfilter import MatchesFilter


# -------------------------------------------------------------------------
#
# Typing modules
#
# -------------------------------------------------------------------------
from typing import Set
from gramps.gen.lib import Person
from gramps.gen.db import Database


# -------------------------------------------------------------------------
#
# IsDescendantOfFilterMatch
#
# -------------------------------------------------------------------------
class IsDescendantOfFilterMatch(IsDescendantOf):
    """Rule that checks for a person that is a descendant
    of someone matched by a filter"""

    labels = [_("Filter name:")]
    name = _("Descendants of <filter> match")
    category = _("Descendant filters")
    description = _(
        "Matches people that are descendants " "of anybody matched by a filter"
    )

    def prepare(self, db: Database, user):
        self.db = db
        self.map: Set[str] = set()
        try:
            if int(self.list[1]):
                first = 0
            else:
                first = 1
        except IndexError:
            first = 1

        self.filt = MatchesFilter(self.list[0:1])
        self.filt.requestprepare(db, user)
        if user:
            user.begin_progress(
                self.category,
                _("Retrieving all sub-filter matches"),
                db.get_number_of_people(),
            )
        for person in db.iter_people():
            if user:
                user.step_progress()
            if self.filt.apply(db, person):
                self.init_list(person, first)
        if user:
            user.end_progress()

    def reset(self):
        self.filt.requestreset()
        self.map.clear()

    def apply(self, db, person):
        return person.handle in self.map
