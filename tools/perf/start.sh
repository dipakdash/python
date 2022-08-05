#!/bin/bash

#python3 runner.py -l info -u test_web_domain_names.txt -t domain --proxyauth
#python3 runner.py -l info -u test_urls.txt -t url --proxyauth 

##python3 runner.py -l info -u test_web_domain_names.txt -t domain --noproxy
##python3 runner.py -l info -u test_web_domain_names.txt -t domain -m multiprocess --noproxy
##python3 runner.py -l info -u test_web_domain_names.txt -t domain -m multithread --noproxy
##python3 runner.py -l info -u test_web_domain_names.txt -t domain -m wrong_option --noproxy

##python3 runner.py -l info -u test_urls.txt -t url --noproxy
##python3 runner.py -l info -u test_urls.txt -t url -m multiprocess --noproxy
##python3 runner.py -l info -u test_urls.txt -t url -m multithread --noproxy
##python3 runner.py -l info -u test_urls.txt -t url -m wrong_option --noproxy

##python3 runner.py -l info -u test_urls.txt -t url
##python3 runner.py -l info -u test_urls.txt -t url -m multiprocess
##python3 runner.py -l info -u test_urls.txt -t url -m multithread
##python3 runner.py -l info -u test_urls.txt -t url -m multithread --load
##python3 runner.py -l info -u test_urls.txt -t url -m multiprocess --load
##python3 runner.py -l info -u test_urls.txt -t url -m multithread --soak
##python3 runner.py -l info -u test_urls.txt -t url -m multiprocess --soak
##python3 runner.py -l info -u test_urls.txt -t url -m wrong_option

##python3 runner.py -l info -u test_web_domain_names.txt -t domain --noproxy
#python3 runner.py -l info -u test_urls.txt -t url --noproxy
##python3 runner.py -l info -u test_web_domain_names.txt -t domain
##python3 runner.py -l info -u 500_domains.txt -t domain

##python3 runner.py -l info -u workload.txt -t url
##python3 runner.py -l info -u workload.txt -t url -m multiprocess
##python3 runner.py -l info -u workload.txt -t url -m multithread
##python3 runner.py -l info -u workload.txt -t url -m multithread --load
python3 runner.py -l info -u workload.txt -t url -m multiprocess --load
##python3 runner.py -l info -u workload.txt -t url -m multithread --soak
##python3 runner.py -l info -u workload.txt -t url -m multiprocess --soak
##python3 runner.py -l info -u workload.txt -t url -m wrong_option
