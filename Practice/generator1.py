#!/usr/bin/python
import time
import random


def people_list(num_people):
    names = ["dipak", "adi", "pinu", "others"]
    majors = ["math", "physics", "english", "arts"]
    result = []
    for i in range(num_people):
        person = {'id':i, 
                  'name':random.choice(names),
                  'major':random.choice(majors)}
        result.append(person)
    return person
    
def people_gen(num_people):
    names = ["dipak", "adi", "pinu", "others"]
    majors = ["math", "physics", "english", "arts"]
    for i in range(num_people):
        person = {'id':i, 
        'name':random.choice(names), 
        'major':random.choice(majors)}
        yield person

#t1 = time.clock()
#people_list(1000000)
#t2 = time.clock()
#print("Took {} seconds for people_list".format(t2-t1))

t1 = time.clock()
people_gen(1000000)
t2 = time.clock()
print("Took {} seconds for people_gen".format(t2-t1))