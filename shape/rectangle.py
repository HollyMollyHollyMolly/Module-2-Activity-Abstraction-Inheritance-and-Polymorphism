"""This module defines the Rectangle class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "23/09/2025"

from .shape import Shape
import math

class Rectangle(Shape):
    """This class represents a rectangle shape."""
    def __init__(self, color: str, length: int, width: int):
        """Initialize the rectangle with a color, length, and width."""
        super().__init__(color)

        if not isinstance(length, int):
            raise TypeError("Length must be numeric.")

        if not isinstance(width, int):
            raise TypeError("Width must be numeric.")  

        #if length <= 0 and width <= 0:
        #   raise ValueError("Length and width must be positive numbers.")
        
        self.length = length
        self.width = width

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return f"the shape color is {self._color}, This rectangle has four sides with the lengths of ({self.length}), ({self.width}), ({self.length}) and ({self.width}) centimeters.)"
    
    def caculate_area(self) -> float:
        """Calculate the area of the rectangle."""
        area = self.length * self.width
        return area
    
    def caculate_perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        perimeter = 2 * self.length + 2 * self.width
        return perimeter