# Write a Python program which accepts the radius of a circle from the user and compute the area.

# First approach
r = float(raw_input("r: "))

print "Radius = %.5f" % round(r, 2)
print "Area = %.5f" % round(22/7.0 * r**2, 2)

# Second approach
from math import pi
print "Area = %.5f" % round(pi * r**2, 2)