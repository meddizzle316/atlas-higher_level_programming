#!/usr/bin/python3
"""a module for the square class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ 
    Square class:
        attributes:
            __size: private variable 
            of square

        methods:
            __init__-- initializes function
            validates size 
            area: returns area
            __str__: customizes string 
            representation
    """
    def __init__(self, size):
        super().integer_validator(self, size)
        super().__init__(size, size)
        self.__size = size
        
    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
