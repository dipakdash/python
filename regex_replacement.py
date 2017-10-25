#!/usr/bin/python

import re
import sys

def regex_replace(input_file, replacement_file):
    infile = input_file
    outfile = replacement_file
    element_attrib_dict = {}
    f = open(infile)
    lines = f.readlines()
    f.close()
      
    # This regex will capture XML Elements and Attributes from the input xml file
    regex1 = '^<([\w|\.|\-|\s]+)\s+'   # This will capture the XML Elements
    regex2 = '\s+([\w|\.|\-|\s]+)='    # This will capture the element Attributes
    pattern1 = re.compile(regex1)
    pattern2 = re.compile(regex2)
    for line in lines:
        if line.strip() and line.strip() not in ['<features>','</features>']:
            match1 = pattern1.findall(line)   # Returns a list containing one item that is the Element
            key = match1[0]
            print key
            match2 = pattern2.findall(line)   # Returns a list containing multiple items that are the Attributes of the element captured in the previous list
            value = match2
            if match1 and match2:
                element_attrib_dict.setdefault(key,[]).append(value)
    
    #print element_attrib_dict(['LogFileManager'])
    f = open("out.txt", "w")
    for (k, v) in element_attrib_dict.iteritems():
        line = k + ' = ' + str(v[0])
        f.write(line)
        f.write("\n")
        #sys.exit(0)
    f.close()
    
if __name__ == "__main__":
    input_file = 'request_features_decoded.xml'
    replacement_file = 'request_features_decoded_replaced.txt'
    regex_replace(input_file, replacement_file)
    