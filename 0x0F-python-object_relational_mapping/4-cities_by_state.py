#!/usr/bin/python3

"""
4-cities_by_states
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
    cur.execute('SELECT cities.id, cities.name, states.name \
        FROM states JOIN cities ON states.id = cities.state_id')
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
