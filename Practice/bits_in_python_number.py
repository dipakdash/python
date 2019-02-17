#!/usr/bin/python

def bits_in_python_number():
    a = 1
    bits = 0
    while a:
        a = a << 1
        print(bits)
        bits = bits + 1
    
if __name__ == "__main__":
    bits_in_python_number()