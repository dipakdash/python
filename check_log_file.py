import os
import sys
import glob

def check_log_file(log_file, search_str):
    directory = "C:\Users\Administrator\Downloads"
    os.chdir(directory)
    f = open(log_file)
    lines = f.readlines()
    f.close()
    found = False
    for line in lines:
        if search_str in line:
            found = True
            break
    return found    
if __name__ == "__main__":
    log_file = sys.argv[1]
    search_str = sys.argv[2]
    print check_log_file(log_file, search_str)