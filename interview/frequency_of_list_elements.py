#!/usr/bin/python

# https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list

# Dictionary Comprehension
# Create a dictionary with (key, value) as (element, frequency)

#a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
#d = {x:a.count(x) for x in a}
#d
#{1: 4, 2: 4, 3: 2, 4: 1, 5: 2}

def frequency_of_list_elements():
    a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
    d = {}
    for item in a:
        if item in d:
            d[item] = d.get(item) + 1
        else:
            d[item] = 1
    for k,v in d.items():
        print(str(k)+':'+str(v))
    
if __name__ == "__main__":
    frequency_of_list_elements()