import os
import fnmatch
import string

def dir_walk(root, pattern='*'):

    result = []

    try:
        names = os.listdir(root)
    except os.error as e:
	raise e
	return result

    pat_list = string.splitfields(pattern, ';')
    
    for name in names:
        fullname = os.path.normpath(os.path.join(root, name))
        if os.path.isfile(fullname):
	    for pat in pat_list:
                if fnmatch.fnmatch(fullname, pat):
                    result.append(fullname)

    return result

if __name__ == "__main__":
    root = "/home/ddash/github/python/"
    #pattern = "*.py"
    pattern = "*.xml"
    names = dir_walk(root, pattern)
    for name in names:
        print name 
