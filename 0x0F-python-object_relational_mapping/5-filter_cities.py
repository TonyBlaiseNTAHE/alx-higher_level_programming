#!/usr/bin/python3

"""
5-filter_cities module
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.Connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM states JOIN cities \
        ON states.id=cities.state_id \
        WHERE states.name = \'{}\' ORDER BY cities.id ASC'.format(sys.argv[4]))
    rows = cur.fetchall()
    n = len(rows)
    i = 0
    for row in rows:
        if (i < n - 1):
            print(row[0], end=', ')
            i += 1
        else:
            print(row[0])
    cur.close()
    db.close()
