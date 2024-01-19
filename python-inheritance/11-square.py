#!/usr/bin/python3
"""a module for the square class"""
Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator(size)
        self.__size = size
    
    def area(self):
        return self.__size * self.__size
        
    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
