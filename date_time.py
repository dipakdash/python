# Write a Python program to display the current date and time.

from datetime import datetime

import time
#http://strftime.org/

print datetime.now()
print datetime.now().strftime('%y-%m-%d %H:%M:%S')
print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print datetime.now().time()

print time.time()
print time.ctime()
print time.ctime()[:3]
print time.ctime()[4:7]
print time.ctime()[-4:]

print time.strftime('%Y%m%d')
print time.strftime('%Y')
print time.strftime('%m')
print time.strftime('%B')
print time.strftime('%d')