#!/usr/bin/python3
"""creates a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""
    def __init__(self, width=0, height=0):
        """Method for initialization of object Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method with width validation, allows width attribe
        manipulation"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter method to retrieve height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attribute with validation,
        allows manipulation"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def perimeter(self):
        """Return perimeter of Rectangle object"""
        if width == 0 or height == 0:
            return
        return ((self.width + self.height) * 2)

    def area(self):
        """Returns area of a Rectangle"""
        if width == 0 or height == 0:
            return
        return (self.width * self.height)

    def __str__(self):
        """Method to print string"""
        if self.width == 0 or self.height == 0:
            return
        else:
            return (f"{'#' * self.width}\n)" * self.height).strip("\n")

    def __repr__(self):
        """Method to return string represenation of obj Rectangle"""
        return (f"Rectangle({self.width}, {self.height})")
