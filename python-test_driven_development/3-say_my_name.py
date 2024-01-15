#!/usr/bin/python3
"""
This is a module practicing the VERY useful doctesting method
"""


def say_my_name(first_name, last_name=""):
    """a function that prints a name"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    full_name = first_name + " " + last_name
    print("My name is {}".format(full_name))
