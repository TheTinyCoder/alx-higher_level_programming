#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN \
                states ON cities.state_id=states.id  ORDER BY cities.id ASC")
    states = cur.fetchall()
    for row in states:
        print(row)
