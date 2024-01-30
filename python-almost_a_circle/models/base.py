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
        """function that converts python lists to json"""
        if not list_dictionaries:
            return "[]"
        if not any(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        converts lists of objects to dictionaries
        and saves as json string to file
        """
        if not list_objs:
            list_objs = []
        with open("Rectangle.json", 'w') as file:
            for i in range(len(list_objs)):
                new_string = cls.to_json_string((list_objs[i].to_dictionary()))
                file.writelines(new_string)
