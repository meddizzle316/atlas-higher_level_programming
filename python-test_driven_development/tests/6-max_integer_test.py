#!/usr/bin/python3
import unittest
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    # If middle element => find another integer
    if list[0] != result and list[-1] != result and len(list) > 2:
        old_result = result
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] != old_result:
                result = list[i]
                break
            i += 1
   
    return result

class TestMaxInt(unittest.TestCase):
    
    def test_max_at_end(self):
        list = [1, 2, 3, 4]
        result = max_integer(list)
        self.assertEqual(result, 4)
    def test_same_value(self):
        list = [1, 1, 1, 1]
        result = max_integer(list)
        self.assertEqual(result, 1)
    def test_negative(self):
        list = [-1, -2, -3, -4]
        result = max_integer(list)
        self.assertEqual(result, -1)
    def test_mixed_negative(self):
        list = [-1, 5, 2, -4]
        result = max_integer(list)
        self.assertEqual(result, 5)
    def test_max_at_beginning(self):
        list = [10, 5, 2, -4]
        result = max_integer(list)
        self.assertEqual(result, 10)
