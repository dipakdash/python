#!/usr/bin/python3

string = input("Enter a string of length 6: ")

if(len(string)<6):
    print("Entered string length is less than 6.")
elif(len(string)>6):
    print("Entered string length is more than 6.")
else:
    print("Good. You entered a string exactly of length 6..")
