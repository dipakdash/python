#!/usr/bin/python

#Q2:
#Frame a data structure to represent a 3*3 Matrices and do following operations:
#E.g.
#M1=
#[1,2,3] 
#[4,5,6]
#[7,8,9]

#M2=
#[3,2,1]
#[6,5,4]
#[9,8,7]
#1) Display the Matrices in 3*3 format as shown above
#2) Produce a Matrices M3 such that M3 = M1+M2 i.e. Numeric Addition of elements of each matrices at same index .Print M3
#E.g. M3=
#[4,4,4]
#[10,10,10]
#[16,16,16]
#3) Transpose Matrices M3 and store in T_M3 , Print T_M3

def matrix2():
    m1 = [[1,2,3], [4,5,6], [7,8,9]]
    m2 = [[3,2,1], [6,5,4], [9,8,7]]
    
    for row in m1:
         for column in row:
             print(column, " ", end="")
         print("\n")
    print("\n")
    
    for row in m2:
        for column in row:
            print(column, " ", end="")
        print("\n")
    print("\n")
    
    result = [] * len(m1)
    for i in range(len(m1)):
        temp = []
        for j in range(len(m1)):
            temp.append(m1[i][j] + m2[i][j])
        result.append(temp)
    
    for row in result:
        for column in row:
            print(column, " ", end="")
        print("\n")
        
    #Using list comprehension
    # https://www.geeksforgeeks.org/python-program-add-two-matrices/
    result = [[m1[i][j] + m2[i][j]  for j in range(len(m1[0]))] for i in range(len(m1))]
  
    for r in result:
        print(r)

if __name__ == "__main__":
    matrix2()