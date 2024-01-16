#!/usr/bin/python3
"""
A module that prints a text with 2 new lines
after specific characters
"""


def text_indentation(text):
    """ prints newlines after specified characters """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(text[i])
            print()
            if text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1
