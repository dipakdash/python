#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="10.44.186.79", #host="localhost", # your host, usually localhost 10.44.186.79:5432
                     user="threat", # your username
                      passwd="ykMyfp2DIE", # your password
                      db="threatdevdb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM camelus_rule_test_specify_rule")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]