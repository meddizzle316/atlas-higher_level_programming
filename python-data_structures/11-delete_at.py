#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(my_list) + 1):
        if i == idx + 1:
            my_list.remove(i)
    return my_list
