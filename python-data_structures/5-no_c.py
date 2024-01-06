#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    if my_string is None:
        pass
    elif len(my_string) > 0:
        new_string = my_string.replace("c","")
        new_string = my_string.replace("C","")
        return new_string
