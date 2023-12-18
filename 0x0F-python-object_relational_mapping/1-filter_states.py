#!/usr/bin/python3
"""
1-filter_states module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = conn.cursor()
    c.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
