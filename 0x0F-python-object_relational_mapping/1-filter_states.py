#!/usr/bin/python3

"""
0-select_states module
"""
import MySQLdb
import sys

if __name__ == '__main__':
	conn = MySQLdb.connect(
			host="localhost",
			port=3306,
			user=sys.argv[1],
			password=sys.argv[2],
			db=sys.argv[3])
	c = conn.cursor()
	c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
	rows = c.fetchall()
	for eachrow in rows:
		print(eachrow)
	c.close()
	conn.close()
