#!/usr/bin/python3

# The *args will give you all function parameters as a tuple
# The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.

def foo(*args, **kwargs):
    print(f'type(args) = {type(args)} , args = {args}')
    print(f'type(kwargs) = {type(kwargs)} , kwargs = {kwargs}')
    print("\n")

if __name__ == "__main__":
    foo(1,2,3, name='dipak', id=475)
    foo(2, 1.57, -17, (1, 2, 3), pi=3.14)
