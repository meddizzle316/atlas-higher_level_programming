#!/usr/bin/python3
"""
module for class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle- inherits from base
    Properties/Attributes:
        width - width
        height - height
        x - ?
        y - ?
    Method:
        __init__: initializes, super from Base
        to get assign Base.id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle with # to stdout"""
        new_list = []
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for i in range(self.height + self.y):
                if i < self.y:
                    print()
                    continue
                for x in range(self.width + self.x):
                    if x < self.x:
                        print(" ", end="")
                        continue
                    print("#", end="")
                print()

    def __str__(self):
        """new string representation"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " +
                f"{self.__width}/{self.__height}")

    # def __iter__(self):
    #     """changes how Rectangle is iterated over"""
    #     for attribute, value in self.__dict__.items():
    #         yield attribute

    def update(self, *args, **kwargs):
        """function that updates Rectangle with new variables"""
        if not any(args):
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns a dictionary representation of Rect"""
        self.__dict__['width'] = self.__dict__.pop('_Rectangle__width')
        self.__dict__['height'] = self.__dict__.pop('_Rectangle__height')
        return self.__dict__
