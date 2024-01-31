#!/usr/bin/python3
"""
has tests for base class
"""
import unittest
from models.base import Base

class Test(unittest.TestCase):
    """Class for unittests on Base class"""
    def test_base_auto_assign_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
    