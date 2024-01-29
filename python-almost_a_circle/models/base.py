#!/usr/bin/python3
"""base module for almost a circle"""
import json


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        if not any(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)
