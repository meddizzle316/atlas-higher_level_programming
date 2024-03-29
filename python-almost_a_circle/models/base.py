#!/usr/bin/python3
"""base module for almost a circle"""
import json
import os


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
        list = []
        with open(f"{cls.__name__}.json", 'w') as file:
            if not list_objs:
                file.writelines("[]")
            else:
                for i in range(len(list_objs)):
                    list.append((list_objs[i].to_dictionary()))
            file.writelines(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the json string
        representation json_string
        """
        list = []
        if not json_string:
            return list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance will all attributes
        already set
        """
        new_object = cls(1, 1)
        for key, value in dictionary.items():
            new_object.update(**dictionary)
            """
            I think you have to put the **before, otherwise
            it doesn't work??
            """
        return new_object

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        new_list = []
        if not os.path.isfile(f"{cls.__name__}.json"):
            return new_list
        with open(f"{cls.__name__}.json", 'r') as file:
            new_list = cls.from_json_string(file.read())
            list_of_new_objects = []
            for i in range(len(new_list)):
                new_object = cls.create(**new_list[i])
                list_of_new_objects.append(new_object)
        return list_of_new_objects
