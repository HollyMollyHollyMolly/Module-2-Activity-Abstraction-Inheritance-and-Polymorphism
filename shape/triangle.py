"""This module defines the Triangle class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "23/09/2025"

from shape.shape import Shape
import math

class Triangle(Shape):
    """This class represents a triangle shape."""
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """Initialize the triangle with a color and three sides."""
        super().__init__(color)


        if not isinstance(side_1, int):
            raise TypeError("Side 1 must be numeric.")

        if not isinstance(side_2, int):
            raise TypeError("Side 2 must be numeric.")  

        if not isinstance(side_3, int):
            raise TypeError("Side 3 must be numeric.")


        if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
            raise ValueError("Sides must be positive numbers.")
        
        if not ((side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1)):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def __str__(self) -> str:
        """Return a string representation of the triangle."""
        return f"the triangle color is (color={self._color}), This triangle has three sides with lengths of {self.side_1}, {self.side_2} and {self.side_3} centimeters.)"
    
    def caculate_area(self) -> float:
        """Calculate the area of the triangle using Heron's formula. sp: semi-perimeter"""
        sp = (self.side_1 + self.side_2 + self.side_3 )/ 2
        area = math.sqrt ((sp * (sp - self.side_1) * (sp - self.side_2) * (sp - self.side_3))) 
        return area
    
    def caculate_perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        p = self.side_1 + self.side_2 + self.side_3 
        return p