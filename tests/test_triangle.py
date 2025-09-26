"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "23/09/2025"

import unittest
from shape.triangle import Triangle 

class TestTriangle(unittest.TestCase):
    """Unit tests for the Triangle class."""

    def test_init_valid(self):
        """Test case 1: Initialization with valid inputs."""
        tri = Triangle("red", 3, 4, 5)
        self.assertEqual(tri._color, "red")
        self.assertEqual(tri.side_1, 3)
        self.assertEqual(tri.side_2, 4)
        self.assertEqual(tri.side_3, 5)

    def test_init_blank_color(self):
        """Test case 2: Initialization with blank color should raise ValueError."""
        with self.assertRaises(ValueError):
            Triangle("", 3, 4, 5)

    def test_init_invalid_side_1(self):
        """Test case 3: Non-integer side_1 should raise TypeError."""
        with self.assertRaises(TypeError):
            Triangle("blue", "three", 4, 5)

    def test_init_invalid_side_2(self):
        """Test case 4: Non-integer side_2 should raise TypeError."""
        with self.assertRaises(TypeError):
            Triangle("blue", 3, "four", 5)

    def test_init_invalid_side_3(self):
        """Test case 5: Non-integer side_3 should raise TypeError."""
        with self.assertRaises(TypeError):
            Triangle("blue", 3, 4, "five")

    def test_str_method(self):
        """Test case 6: __str__ returns formatted string."""
        tri = Triangle("green", 3, 4, 5)
        expected = (
            "The shape color is green. "
            "This triangle has three sides with lengths of 3, 4, and 5 centimeters."
        )
        self.assertEqual(str(tri), expected)

    def test_calculate_area(self):
        """Test case 7: Returns correct area (using Heron's formula)."""
        tri = Triangle("yellow", 3, 4, 5)
        self.assertAlmostEqual(tri.caculate_area(), 6.0)

    def test_calculate_perimeter(self):
        """Test case 8: Returns correct perimeter."""
        tri = Triangle("yellow", 3, 4, 5)
        self.assertEqual(tri.caculate_perimeter(), 12)

if __name__ == '__main__':
    unittest.main()

