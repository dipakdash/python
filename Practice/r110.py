#!/usr/bin/python

# print 8, 6, 4, 2, 0, -2, -4, -6, -8
def print_range():
    x = range(8, -9, -2)
    print(list(x))

if __name__ == "__main__":
    print_range()