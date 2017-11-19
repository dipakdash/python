import os
import sys
import glob

def delete_files(directory, file_type):
    os.chdir(directory)
    if file_type == "log":
        files=glob.glob('*.log')
    if file_type == "tcpdump":
        files=glob.glob('*.trace')
    for f in files:
        os.remove(f)
        
if __name__ == "__main__":
    directory = sys.argv[1]
    file_type = sys.argv[2]
    delete_files(directory, file_type)