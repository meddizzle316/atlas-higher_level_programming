#!/usr/bin/python3
"""A module for task 2; appending text"""


def append_write(filename="", text=""):
    """function that appends text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
