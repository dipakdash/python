#!/usr/bin/python

dict1 = {"dipak":1, "pinu":2, "adi":3}

def yield1():
    for (k, v) in dict1.items():
        yield(k, v)

if __name__ == "__main__":
    print(list(yield1()))
