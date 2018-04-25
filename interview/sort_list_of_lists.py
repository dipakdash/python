#!/usr/bin/python

#Q3.
#Given a list of Lists [[1,30,3],[4,15,6],[5,20,7]]
#Sort it according to the middle element of every List Index.
#So the expected Output should be according to the order of middle elements i.e. 15<20<30
#Output:
#[4,15,6]
#[5,20,7]
#[1,30,3]


def sort_list_of_lists():
    lists = [[1,30,3],[4,15,6],[5,20,7]]
    print(sorted([list for list in lists], key=lambda x: x[1]))
    
if __name__ == "__main__":
    sort_list_of_lists()