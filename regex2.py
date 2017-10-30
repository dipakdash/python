import os
import re

def regex_match(text_file, regex):
    if not os.path.isfile(text_file):
        return "file not found"


    f = open(text_file)
    lines = f.read()
    f.close()
    # The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes the . in a regular expression match all characters, including newlines.   
    p = re.compile(regex, re.DOTALL)
    ret = p.findall(lines)
    return ret 

if __name__ == "__main__":
    my_file = 'regex_file.txt'
    regex1 = r'HTTP/1.1 200 OK.*Via.*192\.168\.10\.20.*192\.168\.10\.10.*'
    regex2 = ""
    print regex_match(my_file, regex1)
    
