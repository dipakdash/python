#!/usr/bin/python3

# Lists can contain duplicates, different data types

numbers = [1,3,5,7,9,17]
letters = ['a', 'b', 'c']

print(f'list numbers = {numbers}')
print(f'list letters = {letters}')

print(f'first element of list numbers is numbers[0] = {numbers[0]}')
print(f'last element of list numbers is numbers[-1] = {numbers[-1]}')

print(f'list numbers + letters = {numbers + letters}')
letters.reverse()
print(f'list letters reversed in place {letters}')

print(f'sliced list numbers, numbers[1:4] = {numbers[1:4]}')
print(f'sliced list numbers reversed, numbers[4:1:-1] = {numbers[4:1:-1]}')
