#!/usr/bin/python3
""" A module to learn inheritance """


class MyList(list):
    """ a custom class for a list """
    
    def print_sorted(self):
        """ prints a sorted list, no return """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
