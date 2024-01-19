#!/usr/bin/python3
"""
Module learning inheritance
has a lookup function

Lookup:
    arg: obj
    return: new list
"""


def lookup(obj):
    """ function that returns a list dictionary """
    return list(dir(obj))
