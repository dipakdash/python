#!/usr/bin/python3

print(f'3 == 5 is {3 == 5}') #False
print(f'3 != 5 is {3 != 5}') #True
print(f'bool(1.732) is {bool(1.732)}') #True
print(f'bool(1.23+7j) is {bool(1.23+7j)}') #True
print(f'bool(0) is {bool(0)}') #False

print(f'bool("bool") is {bool("bool")}') #True
print(f'bool("") is {bool("")}') #False

print(f'str(True) is {str(True)}') #'True'
print(f'str(False) is {str(False)}') #'False'

print(f'int(True) is {int(True)}') #1
print(f'int(False) is {int(False)}') #0

print(f'5 + True is {5 + True}') #True converted to int, 1, and Added to 5 = 6
print(f'10 * False is {10 * False}') #False converted to int, 0 and multiplied to 10 = 0

