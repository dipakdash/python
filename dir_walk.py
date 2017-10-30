#-------------------------------------------------------------------------------
# Copyright (C) 2010 McAfee, Inc.  All rights reserved.
#-------------------------------------------------------------------------------
# Name:        Base Test Class
# Purpose:     This class must be inherited to write a test case
#
# Author:      dipak
#
# Created:     02/08/2012
# Copyright:   (c) dipak 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
def dir_walk( root, recurse=0, pattern='*', return_folders=0 ):
    import fnmatch, string
    # initialize
    result = []

    # must have at least root folder
    try:
        names = os.listdir(root)
    except os.error:
        return result

    # expand pattern
    pattern = pattern or '*'
    pat_list = string.splitfields( pattern , ';' )
    
    # check each file
    for name in names:
        fullname = os.path.normpath(os.path.join(root, name))

        # grab if it matches our pattern and entry type
        for pat in pat_list:
            if fnmatch.fnmatch(name, pat):
                if os.path.isfile(fullname) or (return_folders and os.path.isdir(fullname)):
                    result.append(fullname)
                continue
                
        # recursively scan other folders, appending results
        if recurse:
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                result = result + dir_walk( fullname, recurse, pattern, return_folders )
            
    return result

if __name__ == '__main__':
    files = dir_walk('/home/ddash', 0, '*.py')
    for file in files:
        print os.path.basename(file)
