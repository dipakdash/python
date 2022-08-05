#!/usr/bin/python3

# Order doesn't matter in Sets. No duplicates are there. Can take different data types

my_set = set()
print(f'Printing empty set just now created: {my_set}')
my_set.add("Dipak")
my_set.add(3.14)
my_set.add(False)
my_set.add(5)

print(f'Printing set: {my_set}')
my_set.add("Dipak")
my_set.add(3.14)
my_set.add(False)
my_set.add(5)

print(f'Printing set after trying to add duplicates: {my_set}')
print(f'Printing length of set after trying to add duplicates: {len(my_set)}')

#my_set.remove(6) #Trying to remove non-existing element will throw exception
my_set.discard(6) #Trying to discard non-existing element will not raise any exception
my_set.remove(5)
print(f'Printing set after removing an element 5: {my_set}')

my_set.clear() #Removing all the elements from a set
print(f'Printing set after clearning all the elements: {my_set}')

my_set = set([False, 'Dipak', 3.14, 5]) #Creating a set by pre-populating with a collection of elements
print(f'Printing set after creating this by pre-populating with a collection of elements: {my_set}')

odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

print(f'Union of odds and evens: {odds.union(evens)}')
print(f'Intersection of odds and evens: {odds.intersection(evens)}')
print(f'Intersection of evens and composits: {evens.intersection(composites)}')
print(f'Intersection of evens and primes: {evens.intersection(primes)}')
print(f'Union of primes and composites: {primes.union(composites)}')

print(f'2 in primes: {2 in primes}')
print(f'9 not in evens: {9 not in evens}')
