# Garrulous API
# Authors: Michael Pierre and Richard Meyers

"""
Copyright (C) <year>  <name of author>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import collections
import json

from database import Database

class Friendships(Database):
    def __init__(self):
        super(Messages, self).__init__()

    # Read Friendships By User ID.
    def ReadFriendshipsByUID(self, uid):
        try:
            self.db_cursor.execute("SELECT uid_connected_with FROM friendships WHERE uid=?", (uid))
            rows = self.db_cursor.fetchall()
            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d['uid_connected_with'] = row[0]
                objects_list.append(d)
        except Exception, e:
            raise e
        print uid

    # Delete
    def DeleteFriend(self,uid, friend_uid):
        try:
            self.db_cursor.execute("DELETE FROM friendships WHERE uid= ? AND uid_connected_with=?", \
                (uid, friend_uid))
        except Exception, e:
            raise e