#!/usr/bin/python3
"""
base module for almost a circle
"""


class Base():
    """
    Base Class
    Attributes:
        __nb_objects: number of objects created
    Methods:
        __init__: sets self.id if id is not None
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        initializes Base object
        self.id is id if id is not None
        if id is none
        objects is incremented
        and id becomes nb_objects
        """
        if not id is None: 
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
