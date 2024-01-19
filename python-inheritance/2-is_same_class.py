#!/usr/bin/python3
""" 
A module that contains a function to tell if an object
is an exact instance of the specified class; returns True
"""
def is_same_class(obj, a_class):
    return (type(obj) == a_class)
