#!/usr/bin/python3
"""creates class Rectangle"""


class Rectangle:
    """Defines a class rectangle"""
    def __init__(self, width=0, height=0):
        """Method to initialize a Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for retrieving the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of Rectangle width with validation"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter of the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of Rectangle height with validation"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        """Method to calculate perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return
        return ((self.width + self.height) * 2)

    def area(self):
        """Method to calculate the area of a Rectangle"""
        if self.width == 0 or self.height == 0:
            return
        return (self.width * self.height)

    def __str__(self):
        """Method to print a string"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (f"{'#' * self.width}\n" * self.__height).strip("\n")
        # rectangle_str = ""
        # for _ in range(self.height):
        # rectangle_str += '#' * self.width + '\n'
        # return rectangle_str.rstrip('\n')
