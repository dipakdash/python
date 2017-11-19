# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = str(raw_input("first_name: "))
last_name = str(raw_input("last_name"))

print last_name + " " + first_name

# Reverse string
name = first_name + ' ' + last_name
print name[::-1]