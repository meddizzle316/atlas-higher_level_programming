#!/usr/bin/python3
""" a module that contains inherits from function """

def inherits_from(obj, a_class):
    """true if obj inherited from a_class"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
