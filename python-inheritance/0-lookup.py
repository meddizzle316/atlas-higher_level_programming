#!/usr/bin/python3
"""
Module for learning inheritance
has a lookup function
"""


def lookup(obj):
    """ function that returns a list dictionary"""
    return list(obj.__dict__)
