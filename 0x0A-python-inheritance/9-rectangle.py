#!/usr/bin/python3
"""Defines class BaseGeometry & subclass Rectangle
to inherit its properties
"""


class BaseGeometry:
    """Creates class BaseGepmetry"""
    def area(self):
        """Returns area of a surface"""
	return (self.width * self.height)

    def integer_validator(self, name, value)
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
