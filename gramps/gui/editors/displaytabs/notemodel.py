#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2006  Donald N. Allingham
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
# GTK libraries
#
# -------------------------------------------------------------------------
from gi.repository import Gtk


# -------------------------------------------------------------------------
#
# NoteModel
#
# -------------------------------------------------------------------------
class NoteModel(Gtk.ListStore):
    def __init__(self, note_list, db):
        Gtk.ListStore.__init__(self, str, str, bool, str)
        self.db = db
        for handle in note_list:
            note = self.db.get_note_from_handle(handle)
            text = note.get_preview()
            self.append(
                row=[
                    str(note.get_type()),
                    text,
                    note.get_privacy(),
                    handle,
                ]
            )
