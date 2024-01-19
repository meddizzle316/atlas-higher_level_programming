#!/usr/bin/python3
"""
module about reading files in python
It has a single function 
called read_file 
"""


def read_file(filename=""):
    """reads from a given file and prints"""
    with open(filename, 'r') as file:
        df = file.read()
        print(df, end="")
