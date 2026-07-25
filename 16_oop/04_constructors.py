"""
Constructors

This script demonstrates the __init__() constructor.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area."""

        return self.length * self.width


rectangle = Rectangle(8, 5)

print("Area:", rectangle.area())
