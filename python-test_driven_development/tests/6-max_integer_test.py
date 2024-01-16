#!/usr/bin/python3
import unittest
max_integer = __import__ ('6-max_integer').max_integer
"""Module to find the max integer in a list
"""


class TestMaxInt(unittest.TestCase):
    
    def test_max_at_end(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)
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
    def test_one_element(self):
        list = [7]
        self.assertEqual(max_integer(list), 7)
    def test_empty_list(self):
        list = []
        self.assertEqual(max_integer(list), None)
