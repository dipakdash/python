#-------------------------------------------------------------------------------
# Copyright (C) 2012 McAfee, Inc.  All rights reserved.
#-------------------------------------------------------------------------------
# Name:             traffic
# Purpose:          HTTP/HTTP(s) concurrent request Generator for MWG Testing
#
# Author:           dipak
# Maintainer:	    dipak
#
# Created:          5/Jun/2020
# Last Modified:    11/Jun/2020
#
# Version:	0.1
# -------------------------------------------------------------------------------

#!/usr/bin/python

from Request import *

class Traffic():
    """
    Send HTTP/HTTPS/FTP/SOCKS traffic via Proxy
    """
    def __init__(self):
        pass

    def send_traffic(self, ufilename, ufiletype, multitask, proxyauth, proxy_obj):
        r = Request(ufilename, ufiletype, multitask, proxyauth, proxy_obj)
        #print(list(r.url_http))
        #r.sendftp('ftpuser1@10.213.136.204', 'ftpuser1')
        r.sendhttp()
        #r.sendhttps()
        #r.sendhttp_socks()
        #r.sendhttps_socks()
        #r.sendftp('ftpuser1@10.213.136.204', 'ftpuser1')
        return("Done!")
