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
        """initializes Base object"""
        if not id is None: 
            self.id = id
        Base.__nb_objects += 1
