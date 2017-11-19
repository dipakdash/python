#import pyshark
import os
import subprocess
import sys
import socket
from unidecode import unidecode

# https://thepacketgeek.com/intro-to-pyshark-for-programmatic-packet-analysis/
# https://github.com/eaufavor/pyshark-ssl/blob/master/src/pyshark/capture/file_capture.py
# https://wiki.wireshark.org/SSL
#
# Finally useed the following tshark command to do the job. 
# tshark -o http.ssl.port:443,9090 -nr tcpdump.trace ip.addr == 10.213.136.19 > out.txt
# No need to use pyshark. Just commented and kept for future reference

class Tcpdump:
    def __init__(self, mwg_ip, tcpdump_file, search_str):
        self.tcpdump_files_dir = 'C:/Users/Administrator/Downloads/'
        #self.tcpdump_file = 'tcpdump.trace'
        self.tcpdump_file = tcpdump_file
        self.tcpdump_output = None
        self.tcpdump_ssl_decoded = []
        self.search_str = search_str
        #cap = pyshark.FileCapture(path_to_file)
        #cap = pyshark.FileCapture(path_to_file, only_summaries=True)
        #print type(cap)
        #print cap[1]
        #filtered_cap = pyshark.FileCapture(path_to_file, display_filter='http')
        #f = open('C:/Users/Administrator/Downloads/test.txt', 'w')
        
        self.hostname = socket.gethostname()
        self.src_ip = socket.gethostbyname(self.hostname)
        self.des_ip = mwg_ip
        
        self.cmd_1 = "tshark -o http.ssl.port:443,9090 -nr " + self.tcpdump_file + "  ip.addr == " + self.src_ip

        #for pkt in cap:
            #if (pkt.source == src_ip) and (pkt.destination == des_ip):
            #f.write(str(pkt) + '\n')
        #f.close()
    
    def get_ssl_decoded_client_proxy_packets(self):
        os.chdir(self.tcpdump_files_dir)
        try:
            ret = subprocess.Popen(self.cmd_1, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, env=os.environ)
            output = ret.communicate()[0]
            lines = output.split('\n')
            self.tcpdump_output = lines
        except Exception, e:
            raise Exception(e)
        
    def check_output(self):        
        for line in self.tcpdump_output:
            # NOTE:
            # tshark command output text (extracted from tcpdump files downloaded from MWG UI) contanins some non-ascii characters that Python doesn't print properly
            # Having those non-ascii characters here in this Python file as comment also throws error.
            # So, I have tried to either remove (below line) or replace them with closing matching ascii characters (second line from here)
            #line = ''.join(char for char in line if ord(char) < 128) # line becomes non-ascii. Removes non-ascii characters from line
            line = unidecode(unicode(line, encoding = "utf-8")) #get the most closely matching replacement for any non-ascii character in line
            if line.find(self.search_str) >= 0:
                self.tcpdump_ssl_decoded.append(line)
                
        if len(self.tcpdump_ssl_decoded) > 0:
            print ":".join(self.tcpdump_ssl_decoded)
        else:
            print None            
if __name__ == "__main__":
    mwg_ip = '10.213.136.87'
    tcpdump_file = sys.argv[1]
    search_str = sys.argv[2]
    t = Tcpdump(mwg_ip, tcpdump_file, search_str)
    t.get_ssl_decoded_client_proxy_packets()
    t.check_output()