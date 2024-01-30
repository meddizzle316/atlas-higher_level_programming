#!/usr/bin/python3
"""a module for the class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that updates Square"""
        if not any(args):
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.width = self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass


    def to_dictionary(self):
        """returns a dictionary representation of Rect"""
        attributes = ["id", "size", "x", "y"] 
        """
        I only sort of understand what's going on here
        the getattr function is looking for "size" 
        I know "size" is a property (I set it)
        yet self.__dict__ doesn't print out "size"
        if getattr didn't find size, it would run an error
        so it's finding it. maybe getattr looks at @property
        size, returns self.width(which returns self.__width)
        and uses that value -- because the property tag allows the function to be access "like" an attribute
        which means that getattr can work with "@property" functions as long as they return a value. Would this mean that setattr would also work this way?
        """
        d = {}
        for a in attributes:
            d.update({a: getattr(self, a)})
        return d
