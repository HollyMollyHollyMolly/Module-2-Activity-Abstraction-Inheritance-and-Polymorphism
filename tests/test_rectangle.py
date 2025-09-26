"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "23/09/2025"

import unittest
from shape.rectangle import Rectangle
from shape.shape import Shape

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_init_valid(self):
        """Test case 1: Initialization with valid color, length, and width."""
        rect = Rectangle("red", 5, 3)
        self.assertEqual(rect._color, "red")
        self.assertEqual(rect.length, 5)
        self.assertEqual(rect.width, 3)

    def test_init_blank_color(self):
        """Test case 2: Initialization with blank color should raise ValueError."""
        with self.assertRaises(ValueError):
            Rectangle("", 5, 3)

    def test_init_invalid_length_type(self):
        """Test case 3: Initialization with non-integer length should raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("blue", "five", 3)

    def test_init_invalid_width_type(self):
        """Test case 4: Initialization with non-integer width should raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("blue", 5, "3.5")

    def test_str_method(self):
        """Test case 5: __str__ method returns correct formatted string."""
        rect = Rectangle("green", 4, 6)
        expected = "Rectangle(color=green, length=4, width=6)"
        self.assertEqual(str(rect), expected)

    def test_calculate_area(self):
        """Test case 6: Returns correct area."""
        rect = Rectangle("yellow", 5, 4)
        self.assertEqual(rect.caculate_area(), 20)

    def test_calculate_perimeter(self):
        """Test case 7: Returns correct perimeter."""
        rect = Rectangle("purple", 5, 4)
        self.assertEqual(rect.caculate_perimeter(), 18)

if __name__ == '__main__':
    unittest.main()
