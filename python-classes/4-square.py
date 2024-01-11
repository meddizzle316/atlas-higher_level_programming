#!/usr/bin/python3
"""This is a basic training module designed to teach us how to use classes

"""


class Square:
    """This is a class for a square

    We have a basic init function

    Note:
        Do not include the self parameter

    Args:
       size (int): The first parameter
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size

    def area(self):
        return self._Square__size*self._Square__size
    
    @property
    def size(self):
        return self._Square__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value
