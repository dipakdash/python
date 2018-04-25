# Read name and age from a text file
# create a list of tuples such as [('dipak', '35'), ('pinu', '27'), ('adi', '3')]
# sort the list tuples by age
# [('adi', 3), ('pinu', 27), ('dipak', 35)]
# print the oldest and youngest name (adi and dipak)

f = open("name_age.txt")
lines = f.readlines()
f.close()

list_tuple = []

for line in lines:
    list1 = line.strip().split(" ")
    tuple1 = (list1[0], int(list1[1]))
    list_tuple.append(tuple1)
    
print(list_tuple)
list_tuple_sorted = sorted(list_tuple, key=lambda x:x[1])
print(list_tuple_sorted)

print("Youngest : %s" % (list_tuple_sorted[0])[0])
print("Oldest : %s" % (list_tuple_sorted[-1])[0])