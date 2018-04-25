#!/usr/bin/python

#Q1
#From the command line , take as input  set of 10 numbers. If it is an odd number place it in an odd position and for each even number ,place it in even position .
#E.g. Output {11,6,9,16,3,4,7}

def odd_even_list_placement():
    #num_list = map(int, input("Enter 10 comma seperated numbers ").split(","))
    num_list = [0] * 10
    even = []
    odd = []
    for i in range(10):
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    for i in range(10):
        num = int((input("Enter a number ")).strip())
        if (num%2 == 0):
            #num_list[even.pop()] = num
            num_list[even[0]] = num
            even = even[1:]
        else:
            #num_list[odd.pop()] = num
            num_list[odd[0]] = num
            odd = odd[1:]

    print(*num_list)
    
if __name__ == "__main__":
    odd_even_list_placement()