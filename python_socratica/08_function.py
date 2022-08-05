#!/usr/bin/python3

import math

def volume_sphere(r):
    """Returns the volume of a sphere with radious r."""
    v = (4.0/3.0) * math.pi * r**3
    return v

if __name__ == "__main__":
    r = int(input("Enter the radius of sphere: "))
    print(f'Volume of sphere with radius {r} is: {volume_sphere(r)}')
