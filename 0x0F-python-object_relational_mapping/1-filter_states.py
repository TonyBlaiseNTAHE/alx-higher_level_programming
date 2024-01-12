#!/usr/bin/python3

"""
1-filter_states module
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2], db='hbtn_0e_0_usa')
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                 LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
