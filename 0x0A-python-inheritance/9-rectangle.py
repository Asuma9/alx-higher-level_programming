#!/usr/bin/python3
"""Defines class BaseGeometry & subclass Rectangle
to inherit its properties
"""


class BaseGeometry():
    """Creates class BaseGepmetry"""
    def area(self):
        """Returns area of a surface"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if name & value are integers"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creates a subclass Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Method to create an object Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method to return an area of a surface"""
        return self.__width * self.__height

    def __str__(self):
        """Prints the attributes of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
