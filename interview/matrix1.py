#!/usr/bin/python

#Q2:
#Frame a data structure to represent a 3*3 Matrices and do following operations:

#E.g.
#M1=
#[1,2,3]
#[4,5,6]
#[7,8,9]

#1) Display the Matrices in 3*3 format as shown above
#2) Convert the above metrics into a 3*4 format , with sum of every row , appended as the last element of every row.
#Expected Output

#[1,2,3,6]
#[4,5,6,15]
#[7,8,9,24]


def matrix1():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    
    for row in matrix:
        for column in row:
            print(column, " ", end="")
        print("\n")
        
    for row in matrix:
        row.append(sum(row))
            
    for row in matrix:
        for column in row:
            print(column, " ", end="")
        print("\n")
    
if __name__ == "__main__":
    matrix1()