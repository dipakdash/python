#!/usr/bin/python

# Input sequence of integers. Print True if a distinct pair of numbers who product is odd exists in the list

def findOddPair():
    myinput = input("Enter comma separated numbers: ")
    a = [int(x.strip()) for x in myinput.split(",")]
    print(a)
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                if (a[i] * a[j]) & 1:
                    return True
    return False

if __name__ == "__main__":
    print(findOddPair())