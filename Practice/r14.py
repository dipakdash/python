#!/usr/bin/python

# Sum of square of all odd numbers less than n

def sum_square(n):
    x = sum([i*i for i in range(1, n) if i%2 == 1])
    print(x)

if __name__ == "__main__":
    n = input("Enter a number: ")
    sum_square(int(n))