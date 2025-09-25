"""This module defines the Shape class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "23/09/2025"

from abc import ABC, abstractmethod

class Shape(ABC):
    """This class represents a geometric shape."""
    def __init__(self, color:str):
        """Initialize the shape with a color."""
        color = color.strip()
    
        if not color:
            raise ValueError("Color must not be empty.")
        self._color= color

    def __str__(self) -> str:
        """Return a string representation of the shape."""
        return f"the shape color is (color={self._color})"
    
    @abstractmethod
    def caculate_area(self) -> float:
        """abstract method to Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def caculate_perimeter(self) -> float:
        """abstract method to Calculate the area of the shape."""
        pass

        
    