#!/usr/bin/python3
"""
A module that prints a text with 2 new lines 
after specific characters
"""
def text_indentation(text):
    """ prints newlines after specified characters """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i == "." or i == ":" or i == "?":
            print(i)
            print()
        else:
            print(i, end="")
