#!/usr/bin/python3
import unittest
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
