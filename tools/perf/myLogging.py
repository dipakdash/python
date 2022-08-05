#!/usr/bin/python

import sys
import os
import logging

class MyLogging(object):
    """
    Common Logging module
    """
    def __init__(self):
        pass

    def log(self, level, log_string):
        if level == "info":
            logging.info(log_string)
        if level == "error":
            logging.error(log_string)
        if level == "warning":
            logging.warning(log_string)
        if level == "debug":
            logging.debug(log_string)
        if level == "critical":
            logging.critical(log_string)
        print(log_string)
    
def setup_log_file_name(lglevel, log_file_name):
    """
    Function to setup the testcase like setting up the logging
    with proper settings
    """
    # Set the log level accordingly
    if(lglevel == "debug"):
        logLevel=logging.DEBUG
    elif(lglevel == "info"):
        logLevel=logging.INFO
    elif(lglevel == "warning"):
        logLevel=logging.WARNING
    elif(lglevel == "error"):
        logLevel=logging.ERROR
    elif(lglevel == "critical"):
        logLevel=logging.CRITICAL
    else:
        # Set default level
        logLevel=logging.INFO

    # Set log format with time/date, logLevel and message
    logFormat='%(asctime)s %(levelname)-8s %(message)s'

    # Set date format
    logDateFmt='%d %b %H:%M:%S'

    # Set log file name
    _inputDir = os.path.dirname(os.path.abspath(sys.argv[0]))
    #_logDir = _inputDir + "/Logs"
    _logDir = os.path.join(_inputDir, "Logs")

    # Logs directory exist?
    if not os.path.exists(_logDir):
        os.makedirs(_logDir)

    logFileName = os.path.join(_logDir, log_file_name+".log")

    print(logFileName)

    # Set log file mode as write
    logFileMode='w'
    # Now, configure the logging
    logging.basicConfig(level=logLevel,
            format=logFormat,
            datefmt=logDateFmt,
            filename=logFileName,
            filemode=logFileMode)
