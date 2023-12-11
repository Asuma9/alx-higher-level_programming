#!/usr/bin/python3
"""Creates a class BaseGeometyr"""


class BaseGeometry:
    """Defines BaseGeometry class with integer validator"""
    def area(self):
        """To be used to return the area of a surface"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if object is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
