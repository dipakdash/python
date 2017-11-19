# Write a Python program to get the volume of a sphere with radius 6.

from math import pi

r = input("Radius: ")

print ("Volume = %0.2f") % (4/3.0 * pi * r**3)