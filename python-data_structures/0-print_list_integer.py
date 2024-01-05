#!/usr/bin/python3
def print_list_integer(my_list=[]):
    placeholders = '\n'.join(['{:d}'] * len(my_list)) 
    print(placeholders.format(*my_list))
