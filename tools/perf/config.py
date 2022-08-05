#-------------------------------------------------------------------------------
# Copyright (C) 2012 McAfee, Inc.  All rights reserved.
#-------------------------------------------------------------------------------
# Name:             config
# Purpose:          Configuration settings for concurrent request Generator
#
# Author:           dipak
# Maintainer:       dipak
#
# Created:          11/Jun/2020
# Last Modified:    11/Jun/2020
#
# Version:      0.1
# -------------------------------------------------------------------------------

#!/usr/bin/python

class Proxy:
    ip = '10.57.52.15'
    user = 'dipak'
    password = 'pass'

class LoadTest: # Each base thread spawns further multi-thread or multi-process to do the actual traffic submission
    # Valure more than 5 would cause overhead to create multiple thread/process in each single basethread
    # Use below command to kill any defunt python process
    # ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9
    basethreadcount = 3
