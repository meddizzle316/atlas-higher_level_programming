#!/usr/bin/python3
"""
has tests for base class
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class BaseTest(unittest.TestCase):
    """Class for unittests on Base class"""
    def test_base_auto_assign_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
    def test_base_increment_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)
    def test_signed_id(self):
        base = Base(89)
        self.assertEqual(base.id, 89)
    def test_json_string_none_exists(self):
        base = Base()
        Base.to_json_string(None)

