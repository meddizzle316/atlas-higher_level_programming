#!/usr/bin/python3
"""a module about reading files in python"""

def read_file(filename=""):
    with open('filename', 'r') as file:
        df = file.read()
        print(df)
