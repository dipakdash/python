#!/usr/bin/python3

# Tuples are faster than lists. Lists take more memory than Tuples
# Tuples can't be changed. They are Immutable
# Tuples are created quickly than lists

import sys
import timeit

list1 = [1,2,3,4,5,'a','b','c']
tuple1 = (1,2,3,4,5,'a','b','c')

print(f'Memory size of list1 is {sys.getsizeof(list1)}')
print(f'Memory size of tuple1 is {sys.getsizeof(tuple1)}')

list_test = timeit.timeit(stmt = "[1,2,3,4,5,6,7,8,9]", number=1000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5,6,7,8,9)", number=1000000)

print(f'Time taken to create a List a million times is {list_test}')
print(f'Time taken to create a Tuple a million times is {tuple_test}')

tuple2 = ()
tuple3 = ("a") # A string a
tuple4 = ("b",) # A single element Tuple (b)
tuple5 = ("a", "b", "c")

print(f'tuple2 = {tuple2} , tuple3 = {tuple3} , type(tuple3) = {type(tuple3)} , tuple4 = {tuple4} , type(tuple4) = {type(tuple4)} , tuple5 = {tuple5}')

# Other way to create Tuples
tuple6 = 1,
tuple7 = 2,3
tuple8 = 4,5,6
print(f'tuple6 = {tuple6} , tuple7 = {tuple7} , tuple8 = {tuple8}')

# Tuple assignments
survey1 = ("Dipak", "10", True)
name, experience, knows_python = survey1
print(f'name={name}, experience={experience}, knows_python={knows_python}')

# Tuple access by index
print(f'name={survey1[0]}, experience={survey1[1]}, knows_python={survey1[2]}')
