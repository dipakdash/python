#!/usr/bin/python

#Q2:
#There is a file named "Log.txt" containing raw logs having 100's of email addresses.
#Parse this file "Log.txt", extract all email addresses , and Give the count of the email addresses per domain.

#Output E.g. 

import re

def extract_email_address():
    f = open("Log.txt")
    lines = f.readlines()
    f.close()
    set_address = set()
    
    regex = "[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+"
    p = re.compile(regex)
    for line in lines:
        ret = p.findall(line)
        for email_address in ret:
            set_address.add(email_address)
    list_unique_email_address = list(set_address)
    print(list_unique_email_address)
    
    frequency_dict = {}
    
    for address in list_unique_email_address:
        if address.split("@")[1] in frequency_dict:
            frequency_dict[address.split("@")[1]] = frequency_dict.get(address.split("@")[1]) + 1
        else:
            frequency_dict[address.split("@")[1]] = 1
    print(frequency_dict)

if __name__ == "__main__":
    extract_email_address()