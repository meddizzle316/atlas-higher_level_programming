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
