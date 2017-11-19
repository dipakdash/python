# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

import os
from datetime import date

fdate = date(input("Year: "), input("Month (1 to 12): "), input("Day: "))
ldate = date.today()
days = ldate - fdate
print ("Number of days since date %s is %s") % (str(fdate), str(days))