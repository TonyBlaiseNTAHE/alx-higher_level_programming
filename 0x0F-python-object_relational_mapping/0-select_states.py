#!/usr/bin/python3

"""
script that list all the states from
the database hbtn_0e_0_usa
"""
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    password="1719",
    db="hbtn_0e_0_usa",
)
c = conn.cursor()
c.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = c.fetchall()
for eachrow in rows:
	print(eachrow)
