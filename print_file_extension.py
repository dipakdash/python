# Write a Python program to all unique file extension names inside current directory.
# Sample filename : abc.java 
# Output : java

import os

files = [x for x in os.listdir(".") if os.path.isfile(x)]
#extensions = filter(lambda x: x.split(".")[-1] , files)
extensions = set(map(lambda x: x.split(".")[-1] , files))
print extensions

# one line approach
extensions1 = list(set(map(lambda x: x.split(".")[-1], [y for y in os.listdir(".") if os.path.isfile(y)])))
print extensions1