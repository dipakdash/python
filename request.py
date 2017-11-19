import sys
import requests
import subprocess
from ftplib import FTP
#from HTMLParser import HTMLParser
#from lxml import etree

class Traffic:
    def __init__(self):
        #self.proxy_ip = '10.213.136.87'
        #mwg is mapped to IP inside Windows hosts file
        self.proxy_ip = 'mwg'
        self.proxy_port = '9090'
        self.proxy_port_socks = '1080'
        self.proxy_port_ftp = '2121'
        self.http_proxy  = 'http://' + self.proxy_ip + ':' + self.proxy_port
        self.https_proxy = 'https://' + self.proxy_ip + ':' + self.proxy_port
        self.ftp_proxy   = 'ftp://' + self.proxy_ip + ':' + self.proxy_port
        self.request_type = sys.argv[1] # decides which function to call
        self.content = None
        self.status = None

        self.proxyDict = {
              'http'  : self.http_proxy,
              'https' : self.https_proxy,
              'ftp'   : self.ftp_proxy
            }

        #self.ftp_server_ip = '192.168.20.221'
        self.url_http = ['http://10.213.136.204']
        self.url_https = ['https://api.github.com/events', 'https://www.google.co.in/', 'https://10.213.136.204']
        self.url_icar_http = 'http://www.eicar.org/download/eicar.com.txt'
        self.url_icar_https = 'https://secure.eicar.org/eicarcom2.zip'

        self.socks_cmd_1 = 'curl --socks4 ' + self.proxy_ip + ':' + self.proxy_port_socks + ' http://10.213.136.204'
        self.socks_cmd_2 = 'curl --socks4 ' + self.proxy_ip + ':' + self.proxy_port_socks + ' https://10.213.136.204' + ' --insecure'
        self.ftp_over_http_cmd = 'curl -x ' + self.proxy_ip + ':9090 ' + '-u ftpuser1:ftpuser1 ftp://10.213.136.204/ftp_test.txt'
        
        if self.request_type == "browse_url":
            self.url = sys.argv[2] # the URL to browse
            self.search_str = sys.argv[3] # the string to search inside web content (Example: "The transferred file contained a virus and was therefore blocked.")
        
    def check_content_for_string(self, search_str):
        result = "FAIL" # Default result
        lines = self.content.split('\n')
        for line in lines:
            if (line.strip() == search_str.strip()):
                result = "PASS"
        print result
                
    def browse_url_via_proxy(self):
        resp = requests.get(self.url, proxies=self.proxyDict, verify=False)
        #self.content = resp.text
        self.content = resp.content
        self.status = resp.status_code
        #return html_content
        #print html_content
        #print resp.text
        #print resp.status_code
        #print(dir(resp))
        #print(type(resp))  # => <class 'requests.models.Response'>
        #print(resp.ok)           # => True
        #print(resp.status_code)  # => 200
        #print(resp.headers['content-type'])   # => "text/html"

        #doc = etree.HTML(html_content)
        #data_list = []
        #for td in doc.xpath('//table/tr/td [@class="contentData"]'):
        #    data_list.append((td.xpath('./text()')[0]).strip())
        #return ':'.join(data_list)
        
    def sendhttp(self):
        for url in self.url_http:
            r = requests.get(url, proxies=self.proxyDict)

    def sendhttps(self):
        for url in self.url_https:
            r = requests.get(url, proxies=self.proxyDict, verify=False)          

    def sendhttp_socks(self):
        process = subprocess.Popen(self.socks_cmd_1, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print output[0]

    def sendhttps_socks(self):
        process = subprocess.Popen(self.socks_cmd_2, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print output[0]

    def sendftp(self, user, passwd):
        ftp=FTP()
        ftp.connect(self.proxy_ip, self.proxy_port_ftp)
        ftp.login(user=user, passwd=passwd)
        ftp.dir()
        ftp.retrlines('LIST')
        ftp.quit()

    def sendftpoverhttp(self):
        process = subprocess.Popen(self.ftp_over_http_cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        print output[0]       

if __name__ == "__main__":
    t = Traffic()
    if t.request_type == "browse_url":
        t.browse_url_via_proxy()
        if t.search_str == "":
            print t.status
        else:
            t.check_content_for_string(t.search_str)
    #parser = MyHTMLParser()
    #parser.feed(response)
    #parser.handle_data(response)
    #print response
    #t.sendhttp()
    #t.sendhttps()
    #t.sendhttp_socks()
    #t.sendhttps_socks()
    #t.sendftp('ftpuser1@10.213.137.77', 'ftpuser1')
    #t.sendftpoverhttp()
