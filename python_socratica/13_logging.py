#!/usr/bin/python3

import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
#logging.basicConfig(filename = "log1.txt", lformat = LOG_FORMAT, level = logging.DEBUG, filemode = 'w')
LEVEL = logging.DEBUG
logging.basicConfig(filename = "log1.txt", format = LOG_FORMAT, filemode = 'w') #Default filemode is 'a' that is append
logger = logging.getLogger()

logger.info("This is our first log message")
print(f'logger name = {logger.name}')
print(f'logger level = {logger.level}')

print('Defalt logger levels are: NOTSET=0 , DEBUG=10 , INFO=20 , WARNING=30 , ERROR=40 , CRITICAL=50')
print("The above logger.info didn't write any into the log file log1.txt because the logger level starts with default, 30, that is WARNING")
print("Logger only writes logs with level greater than or equal to the set level")

f = open("log1.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line)

logger.setLevel(LEVEL)
print(f'logger level = {logger.level}')
logger.info(f"This is info log message. logger level = {logger.level}")
logger.warning(f"This is warning log messag. logger level = {logger.level}")
logger.error(f"This is error log messag. logger level = {logger.level}")
logger.critical(f"This is critical log messag, logger level = {logger.level}")

print("Now logger will write all the log messages")
f = open("log1.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line)
