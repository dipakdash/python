#!/usr/bin/python

import psycopg2
import sys

try:
        conn = psycopg2.connect("host='10.44.186.79' dbname='threat_portal' user='threat' password='ykMyfp2DIE'")
        print "Connected to Database"
except:
        print "No Connection"

#cur = conn.cursor()#cursor_factory=psycopg2.extras.DictCursor)
#try:
#        cur.execute('SELECT * FROM camelus_rule_test_specify_rule')
#        rows = cur.fetchall()
#        print "\n Show: \n"
#        for row in rows:
#                print "   ", row
#except:
#        print "Not Working"