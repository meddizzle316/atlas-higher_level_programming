#!/usr/bin/python3
import sys


def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        sys.exit()    
    if len(my_list) > 0:
        placeholders = '\n'.join(['{:d}'] * len(my_list))
        print(placeholders.format(*my_list[::-1]))
