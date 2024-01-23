#!/usr/bin/python3
"""
a module that returns an object 
from Json string
"""
import json


def from_json_string(my_str):
    """returns a json string"""
    return json.loads(my_str)
