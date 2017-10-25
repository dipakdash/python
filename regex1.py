import re
import os
import shutil
import sys
import string
import platform

class Regex:
    """
    This class combines various regex functions into it.
    """

    def __init__(self, file):
        self.file = None
        if os.path.isfile(file):
            self.file = file
        else:
            sys.exit("File NOT found : %s " % file)

    def print_file(self):
        f = open(self.file)
        lines = f.readlines() # This returns a list of lines
        #lines = f.read() # This returns a string of lines
        f.close()

        for line in lines:
            print line

    def find_string(self):
        f = open(self.file)
        lines = f.read()
        f.close()

        print lines
        #pattren = "Rule __CT fired"
        pattren = "^cid:[0-9a-f]{4}\$[0-9a-f]{8}\$[0-9a-f]{8}@"
        p = re.compile(pattren)
        lst = p.findall(lines)
        #print len(lst)
        print lst

        


if __name__ == "__main__":
    #if platform.system() == "Windows":
    #    file = 'D:/python/camelus_logs.log'
    #elif platform.system() == "Linux":
    #    file = '/home/python/camelus_logs.log'
    #else:
    #    print "Unsupported platform"
    #    sys.exit(1);
    
    #file = 'D:/python/camelus_logs.log'
    file = 'D:/python/regex_input_file.txt'
    obj = Regex(file)
    #obj.print_file()
    obj.find_string()
