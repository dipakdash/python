#!/usr/bin/python

#Q2:
#Frame a data structure to represent a 3*3 Matrices and do following operations:
#E.g.
#M1=
#[1,2,3] 
#[4,5,6]
#[7,8,9]

#https://www.geeksforgeeks.org/transpose-matrix-single-line-python/

def matrix_transpose():
   m = [[1,2,3], [4,5,6], [7,8,9]]
   
   for row in m:
       print(row)
       
   print("\n")   
   
   mt = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
   
   for row in mt:
       print(row)
           

if __name__ == "__main__":
    matrix_transpose()