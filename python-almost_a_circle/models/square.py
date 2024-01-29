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
