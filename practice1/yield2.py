#!/usr/bin/python

def yield2():
    yield 15
    yield "some string"
    yield 1.15
    yield [1, 2, 3]

if __name__ == "__main__":
    print(list(yield2()))
