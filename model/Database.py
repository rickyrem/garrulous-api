# Garrulous API
# Authors: Michael Pierre and Richard Meyers

"""
Copyright (C) 2015

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

import sqlite3
import os
import logging


class Database(object):
    def __init__(self):
        super(Database, self).__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(os.path.dirname(base_dir), "database")
        db_path = os.path.join(db_path, "garrulous.db")
        self.conn = sqlite3.connect(db_path)
        self.db_cursor = self.conn.cursor()

    def write(self, sql):
        """
        Use this method for queries that do not return rows.
        :param sql:
        :return:
        """
        try:
            with self.conn:
                self.conn.execute(sql)
        except sqlite3.IntegrityError:
            print "Could not run sql: " + sql

    def query(self, sql):
        """
        Only use this when a query returns rows.
        :param sql:
        :return:
        """
        try:
            self.db_cursor.execute(sql)
            return self.db_cursor.fetchall()
        except sqlite3.IntegrityError:
            print "Could not run sql: " + sql


