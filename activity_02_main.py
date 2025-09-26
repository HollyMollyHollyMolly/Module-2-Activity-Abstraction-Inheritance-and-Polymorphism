""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nguyen Dang Thai Ha"

from shape.triangle import Triangle
from shape.shape import Shape
from shape.rectangle import Rectangle

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

# 1. Create an empty list of Shape objects
shapes = []

# 2. Create a Triangle instance and append it
tri1 = Triangle("red", 3, 4, 5)
shapes.append(tri1)

# 3. Create a Rectangle instance and append it
rect1 = Rectangle("blue", 6, 7)
shapes.append(rect1)

# 4. Create 3 additional shapes and append them
tri2 = Triangle("green", 5, 5, 6)
shapes.append(tri2)

rect2 = Rectangle("yellow", 8, 3)
shapes.append(rect2)

tri3 = Triangle("purple", 7, 10, 5)
shapes.append(tri3)

# 5. Iterate through the list and print details
for shape in shapes:
    print(str(shape))
    print(f"Area: {shape.caculate_area():.2f}")
    print(f"Perimeter: {shape.caculate_perimeter():.2f}")
    print()  # blank line for readability



if __name__ == "__main__":
    main()