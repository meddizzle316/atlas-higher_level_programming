#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    elif len(my_list) > 0:
        placeholders = '\n'.join(['{:d}'] * len(my_list))
        print(placeholders.format(*my_list[::-1]))
