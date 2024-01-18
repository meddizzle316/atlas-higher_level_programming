#!/usr/bin/python3
"""
A module to learn inheritance
it's going to focus on simple 
examples first
"""


class MyList(list):

    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
