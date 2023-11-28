#!/usr/bin/python3
"""Creates a Rectangle class"""


class Rectangle:
    """Define class Rectangle with width & height attributes"""
    def __init__(self, width=0, height=0):
        """Initializes object instances for class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter to width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width of the Rectangle"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Getter to height of the Rectangle"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        """Calculates perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def area(self):
        """Method to calculate area of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height)
