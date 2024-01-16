#!/usr/bin/python3
"""
A module focused on learned more about python classes
"""


class Rectangle:
    """A class for a rectangle like object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        return self.height * self._width

    def perimeter(self):
        if self._height == 0 or self.width == 0:
            return 0
        return (self._height * 2) + (self.width * 2)

    def __str__(self):
        new_list = []
        if self.width == 0 or self.height == 0:
            return '\n'
        else:
            for i in range(self._height):
                for x in range(self._width):
                    new_list += '#'
                if not i == self._height - 1:
                    new_list += '\n'
        return ''.join(["".join(sublist) for sublist in new_list])
