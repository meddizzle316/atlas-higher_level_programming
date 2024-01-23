#!/usr/bin/python3
"""
writes an object to a text file
using json respresentation
"""
import json


def save_to_json_file(my_obj, filename):
    """function that saves an obj to json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
