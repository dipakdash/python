#!/usr/bin/python

import sys
sys.path.append('/home/ddash/python/')
import os
import datetime
import config
from optparse import OptionParser
from config import *
from traffic import Traffic
from myLogging import setup_log_file_name

def generate_traffic(ufilename, ufiletype, multitask, proxyauth, noproxy, load, soak):
    if noproxy is None: # That is tester wants to browse via Proxy
        proxy_obj = Proxy
        print("Sending traffic through proxy ++++++++++++++++++++++++++++++++++++++++++++++++++")
    else: # Tester wants to browse directly without Proxy
        proxy_obj = None
        proxyauth = None
        print("Sending traffic without proxy ++++++++++++++++++++++++++++++++++++++++++++++++++")

    t = Traffic()
    if load:
        import concurrent.futures
        print("Load testing started ++++++++++++++++++++++++++++++++++++++++++++++++++")
        load_test_obj = LoadTest
        basethreadcount = load_test_obj.basethreadcount # Each base thread spawns further multi-thread or multi-process to do the actual traffic submission
        print(f'Base thread count is {basethreadcount}')
        #with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #with concurrent.futures.ProcessPoolExecutor() as executor:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(t.send_traffic, ufilename, ufiletype, multitask, proxyauth, proxy_obj) for _ in range(basethreadcount)]
            #for f in concurrent.futures.as_completed(results):
            #    print(f.result())    
    elif soak:
        print("Soak testing started ++++++++++++++++++++++++++++++++++++++++++++++++++")
        while 1:
            if not os.path.isfile("nosoak"):
                t.send_traffic(ufilename, ufiletype, multitask, proxyauth, proxy_obj)
            else:
                break
    else:
        t.send_traffic(ufilename, ufiletype, multitask, proxyauth, proxy_obj)

if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog -l [loglevel] -u [url_file_name] -t [url_file_type] -m [multitask] [--proxyauth] [--noproxy]")
    parser.add_option("-l", "--loglevel", dest="lglevel", choices=["info", "warning" , "error" , "critical" , "debug"], help="Loglevel: info|warning|error|critical|debug [default: info]", default="info", metavar="loglevel")
    parser.add_option("-u", "--url_file_name", dest="ufilename", help="url_file_name", metavar="ufilename")
    parser.add_option("-t", "--url_file_type", dest="ufiletype", help="url_file_type", metavar="ufiletype")
    parser.add_option("-m", "--multitask", dest="multitask", choices=["none", "multiprocess", "multithread"], help="multitask", default="none", metavar="multitask")
    parser.add_option("--proxyauth", action="store_true", dest="proxyauth")
    parser.add_option("--noproxy", action="store_true", dest="noproxy")
    parser.add_option("--load", action="store_true", dest="load")
    parser.add_option("--soak", action="store_true", dest="soak")

    (options, args) = parser.parse_args()

    lglevel = options.lglevel

    if not options.ufilename:
        parser.error("URL file name not passed")
    else:
        if not os.path.exists(options.ufilename):
            parser.error("URL file %s doesn't exist:" % (options.ufilename))
    if not options.ufiletype:
        parser.error("URL file type not passed")

    ufilename = options.ufilename
    ufiletype = options.ufiletype
    multitask = options.multitask
    # If --proxyauth is passed then proxyauth=True otherwise proxyauth=None
    proxyauth = options.proxyauth
    noproxy = options.noproxy
    load = options.load
    soak = options.soak

    now = datetime.datetime.now()
    time_now = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) + "_" + os.path.splitext(ufilename)[0]

    log_file_name = time_now
    setup_log_file_name(lglevel, log_file_name)

    generate_traffic(ufilename, ufiletype, multitask, proxyauth, noproxy, load, soak)
