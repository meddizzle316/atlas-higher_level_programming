#!/usr/bin/python3
"""
Module learning inheritance
has a lookup function

Lookup:
    arg: obj
    return: new list
"""


Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """a module for square class, inherits from rectangle"""
    def __init__(self, size):
        super().integer_validator(size)
        self.__size = size
    
    def area(self):
        return self.__size * self.__size
        
    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
