# Write a Python program to print the calendar of a given month and year.

import calendar

month_list = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}

y = int(raw_input("Enter Calendar Year: ").strip())
m = int(raw_input("Enter Calendar Month (1 to 12): ").strip())
print calendar.month(y, m)