#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0   # class attribute

    def __init__(self, width=0, height=0):
        """MEthod to initialize object rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set width with validation test"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Retrieves height of rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height with a validation test"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        """Methode to return perimeter of obj rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def area(self):
        """Method to return area of rectangle obj"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height)

    def __str__(self):
        """Method to print rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (f"{'#' * self.widht}\n" * self.height).strip("\n")

    def __repr__(self):
        """Method to return string rep of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method to detect instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
