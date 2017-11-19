# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

my_input = str(raw_input("Enter comma-separated numbers: "))

my_list = [int(x) for x in my_input.split(",") if x.strip().isdigit()]
my_tuple = tuple([int(x) for x in my_input.split(",") if x.strip().isdigit()])

# Using map
my_list1 = map(int, my_input.split(","))
my_tuple1 = tuple(map(int, my_input.split(",")))

print my_input
print my_list
print my_tuple

print my_list1
print my_tuple1