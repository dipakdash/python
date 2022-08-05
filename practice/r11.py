#!/usr/bin/python

def is_multiple(n, m):
    if n%m == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(is_multiple(27, 3))