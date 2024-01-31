#!/usr/bin/python3
"""
has tests for base class
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
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
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")
    def test_json_string_empty_list(self):
        base = Base()
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
    def test_from_json_string_None(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string([]), [])
    
class RectangleTest(unittest.TestCase):
    """Class for unittests on Rectangle Class"""
    def test_Rectangle_only_width_and_height_exists(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
    def test_Rectangle_without_y(self):
        r1 = Rectangle(1, 2, 3)
        self.assertIsNotNone(r1)
    def test_all_attributes_Rectangle_exists(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r1)
    def test_Rectangle_width_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
    def test_Rectangle_height_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")
    def test_Rectangle_x_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "3")
    def test_Rectangle_y_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")
    def test_Rectangle_extra_parameter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)
    def test_Rectangle_width_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
    def test_Rectangle_height_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
    def test_Rectangle_width_above_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
    def test_Rectangle_height_above_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
    def test_Rectangle_x_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3)
    def test_Rectangle_y_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)
    def test_Rectangle_area(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
    def test_Rectangle_str(self):
        r1 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 5/5')
    def test_Rectangle_display_without_x_y(self):
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "#\n")
    def test_Rectangle_display(self):
        r1 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n\n  ##\n  ##\n")
    def test_Rectangle_to_dictionary(self):
        r1 = Rectangle(2, 2, 2, 2, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'id': 1, 'width': 2, 'height': 2, 'x': 2, 'y': 2} )
    def test_Rectangle_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(89)
            exp_output = "[Rectangle] (89) 10/10 - 10/10\n"
            print(r1)
            self.assertEqual(fake_out.getvalue(), exp_output)
