#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle:
    """Defines class Rectangle"""
    def __init__(self, width=0, height=0):
        """Method to initialize object Rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter with height validation"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Return value of width"""
        return self.__width

    def width(self, value):
        """Sets width attribute with validation"""
        self.__width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def perimeter(self):
        """Method to return perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def area(self):
        """Method to return area of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height)

    def __str__(self):
        """Method to print Rectangle using '#'"""
        if self.width == 0 or self.height == 0:
            return ""
        return (f"{'#' * self.width}\n" * self.height).strip("\n")

    def __repr__(self):
        """Method to print string representation of Rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method to detect instance deletion"""
        print("Bye rectangle...")
