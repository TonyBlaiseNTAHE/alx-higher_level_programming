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
        WHERE states.name =%s ORDER BY cities.id ASC', (sys.argv[4],))
    rows = cur.fetchall()
    lst = list(row[0] for row in rows)
    print(', '.join(lst))
    cur.close()
    db.close()
