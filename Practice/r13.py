#!/usr/bin/python

def minmax(list):
    minmax_tuple = ()
    min = max = list[0]
    for num in list:
        if num < min:
            min = num
        if num > max:
            max = num
    minmax_tuple = minmax_tuple + (min,)
    minmax_tuple = minmax_tuple + (max,)
    print(minmax_tuple)
    
if __name__ == "__main__":
    minmax([2,1,3,1,4])
    minmax([1,1,1,1,1])
    minmax([2,3,5,1,4])
    minmax([5,1,5,1,5])