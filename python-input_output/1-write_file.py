#!/usr/bin/python3
"""a module for writing text to files"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8'):
        return (filename.write(text))
