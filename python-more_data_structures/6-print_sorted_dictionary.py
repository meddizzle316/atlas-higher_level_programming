#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items_list = a_dictionary.items()
    sorted_list = sorted(items_list)
    for i in range(len(sorted_list)):
        key, value = sorted_list[i]
        print("{}: ".format(key), end="")
        print(value)
