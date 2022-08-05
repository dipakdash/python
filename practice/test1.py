my_name = input("Enter your first name and last name: ")
name = my_name.split()
print(" ".join(name[::-1]))