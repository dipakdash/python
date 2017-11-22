# Use map and range to print suqare of a list [0, 1, 2, 3, 4]

list1 = map(lambda x: x**2, [y for y in range(5)])

for x in list1:
    print(x)