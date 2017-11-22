# map and list comprehension

# Will return:
# >>> list1
# [0, 1, 4, 9, 16]

list1 = map(lambda x: x**2, [y for y in xrange(5)])