#!/usr/bin/python

import sys
sys.path.append('/home/ddash/python/')
import concurrent.futures
import multiprocessing
import requests
from requests.auth import HTTPProxyAuth
import subprocess
from ftplib import FTP
import time
from myLogging import MyLogging
from functools import partial

class Request(MyLogging):
    def __init__(self, ufilename, ufiletype, multitask, proxyauth=None, proxy_obj=None):
        self.url_file = ufilename
        self.url_file_type = ufiletype
        self.multitask = multitask
        self.proxy_port = '9090'
        self.proxy_port_socks = '1080'
        self.proxy_port_ftp = '2121'

        #self.ftp_server_ip = '192.168.20.221'
        self.url_http = self.create_url_dict(self.url_file_type, False)
        self.url_https = self.create_url_dict(self.url_file_type, True)

        self.proxy_obj = proxy_obj

        if self.proxy_obj:
            self.proxyauth = proxyauth
            self.proxy_ip = self.proxy_obj.ip

            if self.proxyauth:
                self.proxy_auth_user = self.proxy_obj.user
                self.proxy_auth_password = self.proxy_obj.password
                self.auth = HTTPProxyAuth(self.proxy_auth_user, self.proxy_auth_password)
                self.http_proxy  = 'http://' + self.proxy_auth_user + ':' + self.proxy_auth_password + '@' + self.proxy_ip + ':' + self.proxy_port
                self.https_proxy = 'https://' + self.proxy_auth_user + ':' + self.proxy_auth_password + '@' + self.proxy_ip + ':' + self.proxy_port
                self.ftp_proxy   = 'ftp://' + self.proxy_auth_user + ':' + self.proxy_auth_password + '@' + self.proxy_ip + ':' + self.proxy_port
            else:
                self.http_proxy  = 'http://' + self.proxy_ip + ':' + self.proxy_port
                self.https_proxy = 'https://' + self.proxy_ip + ':' + self.proxy_port
                self.ftp_proxy   = 'ftp://' + self.proxy_ip + ':' + self.proxy_port

            self.proxyDict = {
              'http'  : self.http_proxy,
              'https' : self.https_proxy,
              'ftp'   : self.ftp_proxy
              }

            self.socks_cmd_1 = 'curl --socks4 ' + self.proxy_ip + ':' + self.proxy_port_socks + ' http://10.213.136.204'
            self.socks_cmd_2 = 'curl --socks4 ' + self.proxy_ip + ':' + self.proxy_port_socks + ' https://10.213.136.204' + ' --insecure'
            self.ftp_over_http_cmd = 'curl -x ' + self.proxy_ip + ':9090 ' + '-u ftpuser1:ftpuser1 ftp://10.213.136.204/readme.txt'

    def create_url_dict(self, url_file_type, https):
        f = open(self.url_file)
        lines = f.readlines()
        f.close()
        if url_file_type == "url":
            for line in lines:
                yield(line.strip())
        if url_file_type == "domain":
            for line in lines:
                if https:
                    yield('https://' + line.strip())
                else:
                    yield('http://' + line.strip())

    def _log_sendhttp(self):
        if self.proxy_obj:
            self.log("info", "Making HTTP Requests via Proxy %s" % self.proxy_ip)
        else:
            self.log("info", "Making direct HTTP Requests without Proxy")

        if (self.multitask == "none"):
            self.log("info", "Making sequential Web requests. No multiprocessing or multithreading applied")
        else:
            if self.multitask == "multiprocess":
                self.log("info", "Applying python multiprocessing")
            if self.multitask == "multithread":
                self.log("info", "Applying python multithreading")

    def _log_response(self, result):
        self.log("info", "Requesting URL: %s    Response Status_Code: %s" % (result.url, result.status_code))
        #print(dir(result))

    def _log_time(self, start, finish):
        self.log("info", f'Finished in {round(finish-start, 2)} second(s)')

    def sendhttp(self):
        self._log_sendhttp()
        if self.proxy_obj:
            #This alternative to pass keyword arguments into map function as we can't pass a keyword argument (proxies=self.proxyDict) directly into map function
            mapfunc = partial(requests.get, proxies=self.proxyDict)

            start = time.perf_counter()
            if (self.multitask == "none"):
                for url in list(self.url_http):
                    result = requests.get(url, proxies=self.proxyDict)
                    self._log_response(result)
                    #print(r.__dict__)
                    #print(r.text)
            else:
                if self.multitask == "multiprocess":
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        results = executor.map(mapfunc, list(self.url_http))
                        for result in results:
                            self._log_response(result)
                if self.multitask == "multithread":
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        results = executor.map(mapfunc, list(self.url_http))
                        for result in results:
                            self._log_response(result)
            finish = time.perf_counter()
            self._log_time(start, finish)
        else:
            start = time.perf_counter()
            if (self.multitask == "none"):
                for url in list(self.url_http):
                    result = requests.get(url)
                    self._log_response(result)
            else:
                if self.multitask == "multiprocess":
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        results = executor.map(requests.get, list(self.url_http))
                        for result in results:
                            self._log_response(result)
                if self.multitask == "multithread":
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        results = executor.map(requests.get, list(self.url_http))
                        for result in results:
                            self._log_response(result)
            finish = time.perf_counter()
            self._log_time(start, finish)

    def sendhttps(self):
        if self.proxy_obj:
            self.log("info", "Sending HTTPS Requests via Proxy %s" % self.proxy_ip)
            for url in list(self.url_https):
                r = requests.get(url, proxies=self.proxyDict, verify=False)
                self.log("info", "Requesting HTTPS URL: %s    Response Status_Code: %s" % (url, r.status_code))
        else:
            self.log("info", "Sending direct HTTPS Requests without Proxy")
            for url in list(self.url_https):
                r = requests.get(url, verify=False)
                self.log("info", "Requesting HTTPS URL: %s    Response Status_Code: %s" % (url, r.status_code))

    def sendhttp_socks(self):
        process = subprocess.Popen(self.socks_cmd_1, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print(output[0])

    def sendhttps_socks(self):
        process = subprocess.Popen(self.socks_cmd_2, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print(output[0])

    def sendftp(self, user, passwd):
        ftp=FTP()
        ftp.connect(self.proxy_ip, int(self.proxy_port_ftp))
        ftp.login(user=user, passwd=passwd)
        ftp.dir()
        ftp.retrlines('LIST')
        ftp.quit()

    def sendftpoverhttp(self):
        process = subprocess.Popen(self.ftp_over_http_cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print(output[0])
