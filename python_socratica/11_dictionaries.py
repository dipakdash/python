#!/usr/bin/python3

# Dictionaries are not ordered. Can contain different types of data

post1 = {"user_id":209, "message":"E09 A11 B23 D15", "language": "English"}
print(f'Printing dictionaly post1 {post1}')
print(f'Printing dictionary key value post1["message"] = {post1["message"]}')

post1["name"] = "Dipak"
print(f'Printing dictionaly post1 {post1}')

post2 = dict(name="Adi", age=7, school="Euro School")
print(f'Printing dictionaly post2 {post2}')

print("Using dictionary get method to handle any key that is not present inside dictionary")
grade = post2.get("grade", None) # Try to access a key and return value None if the key is not present inside the dictionary
print(f'Printing dictionaly key value post2["grade"] = {grade}. The dictionary is {post2}')

print("Using exception handling to check if a key accessed is not present inside the dictionary")
try:
    print(post2["section"])
except KeyError:
    print(f'key "section" is not found inside dictionary post2 {post2}')

print("Iterating over a dictionary key value pairs. Using for (k, v) in post1.items()")
for (k, v) in post1.items():
    print(f'{k} = {v}')

print("Iterating over a dictionary key value pairs. Using for k in post1.keys()")
for k in post1.keys():
    print(f'{k} = {post1[k]}')

print('Using pop dictionary method: post1.pop("name")')
post1.pop("name")
print(f'Printing dictionaly post1 {post1}')

print('Using popitem dictionary method: post1.popitem()')
post1.popitem()
print(f'Printing dictionaly post1 {post1}')

print('Using clear dictionary method: post1.clear()')
post1.clear()
print(f'Printing dictionaly post1 {post1}')
