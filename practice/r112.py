#!/usr/bin/python

# Print random element from a list

import random

def random_choice(my_list):
    print(my_list[random.randint(0,len(my_list)-1)])
    print(my_list[random.randrange(0, len(my_list)-1, 2)])
    
if __name__ == "__main__":
    random_choice([11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999])