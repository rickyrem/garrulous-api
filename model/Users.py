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

import collections
import hashlib

from Database import Database

class Users(Database):
    def __init__(self):
        super(Users, self).__init__()

    # Create user table is not exist.    
    def createIfNotExists(self):
        self.write("""CREATE TABLE IF NOT EXISTS `users` (
          `uid` INTEGER PRIMARY KEY AUTOINCREMENT,
          `username` TEXT,
          `first_name` TEXT,
          `last_name` TEXT,
          `email` TEXT,
          `phone` TEXT,
          `password` TEXT
        )""")

    # Create
    # Create New User
    def createUser(self, user_name, password, first_name=None, last_name=None, email=None, phone=None):
        #set the datejoined column from inside this method
        self.write("INSERT INTO users (first_name,last_name,email,password,phone) "
                   "VALUES (%s,%s,%s,%s,%s) " % (first_name, last_name, email, hashlib.md5(password),phone))


    def updateUserByUid(self, uid, user_name=None, password=None, first_name=None, last_name=None, email=None,
                        phone=None):
        # This needs to build the query out of the amount of parameters that exist. That way a all the existing
        # data doesn't get overwritten.
        self.write("UPDATE users SET first_name=%s, last_name=%s, email=%s, password=%s \
WHERE uid=%s" % (first_name, last_name, email, password, uid))

    # Read All Users
    def getUsers(self):
        # We are not returning all the rows
        # We definitely don't want to return the password column, that is only used for auth.
        # There should be the option of passing in the row quantity.
        rows = self.query("SELECT uid, username, first_name, last_name, email FROM users")
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['uid'] = row[0]
            d['username'] = row[1]
            d['first_name'] = row[2]
            d['last_name'] = row[3]
            d['email'] = row[4]
            objects_list.append(d)
        return objects_list

    # Read User Information By User ID.
    def getUserByUID(self, uid):
        rows = self.query('SELECT uid, first_name, last_name, email FROM users WHERE uid=%s' % uid)
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['uid'] = row[0]
            d['username'] = row[1]
            d['first_name'] = row[2]
            d['last_name'] = row[3]
            d['email'] = row[4]
            objects_list.append(d)
        return objects_list

