#!/usr/bin/python3
"""Defines a Rectangle module"""


class BaseGeometry:
    """Creates a class Basegeometry"""
    def area(self):
        """Returns area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if name is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creates class Rectangle with privates width & height attributes"""
    def __init__(self, width, height):
        """Method to initiate class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method to return area of surface"""
        return self.__width * self.__height

    def __str__(self):
        """prints attributes of the object"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Creates a square object"""
    def __init__(self, size):
        """Method to initiate object square"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area"""
        return self.__size * self.__size
