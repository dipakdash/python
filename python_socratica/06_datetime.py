#!/usr/bin/python3

import datetime

adi_dob = datetime.date(2014, 6, 26)
print(f'Adi date of birth is {adi_dob}, year={adi_dob.year} month={adi_dob.month} day={adi_dob.day}')
dt = datetime.timedelta(100)
print(f'Date 100 days after Adi DoB is {adi_dob + dt}')
dt = datetime.timedelta(-100)
print(f'Date 100 days before Adi DoB is {adi_dob + dt}')

message = "Adi was born on {:%A, %B %d, %Y}"
print(message.format(adi_dob))

birth_date = datetime.date(2014, 6, 26)
birth_time = datetime.time(10, 42, 17)
birth_datetime = datetime.datetime(2014, 6, 26, 10, 42, 17)
print(f'Adi birth date is {birth_date}')
print(f'Adi birth time is {birth_time}')
print(f'Adi birth date and time is {birth_datetime}')
print(f'Adi birth hour={birth_time.hour} minute={birth_time.minute} second={birth_time.second}')

now = datetime.datetime.today()
print(f'Now is {now}')  #2021-09-12 16:53:45.392686
print(f'Now microseconds = {now.microsecond}') #392686

independence_day = "15/8/1947"
republic_day = "26/1/1950"
independence_day_datetime = datetime.datetime.strptime(independence_day, "%d/%m/%Y") # String to datetime object conversion
republic_day_datetime = datetime.datetime.strptime(republic_day, "%d/%m/%Y") # String to datetime object conversion
print(f'Independence day was on {independence_day_datetime}')
print(f'Republic day was on {republic_day_datetime}')
