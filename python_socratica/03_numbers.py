#!/usr/bin/python3

# Three types of numbers in python3: int, float, complex
# In python int, no size limit, no overflows
# j in python is square root of -1 used to make complex numbers
import sys

n = 213
e = 2.718
z = 2 - 6.1j

print(f'sys.maxint = {sys.maxint}')
print(type(n))
print(type(e))
print(type(z))

print(n)
print(e)
print(z.real)
print(z.imag)
