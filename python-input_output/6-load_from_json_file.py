#!/usr/bin/python3
"""
A module with a function
to create a object from json
"""
import json


def load_from_json_file(filename):
    """returns Py Object from Json"""
    with open(filename, 'r') as file:
        return json.load(file)
