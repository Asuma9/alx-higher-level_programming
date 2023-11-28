#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a class rectangle with private attribute"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter with width validation"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter with width validation"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter with height validation"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
