#!/usr/bin/python3
"""
This is a basic module in which we print a square and in which that function is tested
"""

def print_square(size):
    """ A function that prints a square """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
