# Ask user to input comma seperated numbers from comamndline and convert them into a list of squared numbers

list1 = map(lambda x: x**2, [y for y in map(int, raw_input("enter comma seperated numbers: ").split(","))])
print(list1)