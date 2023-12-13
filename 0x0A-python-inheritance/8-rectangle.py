#!/usr/bin/python3
"""Create parent class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """Defines parent class BaseGeometry"""
    def area(self):
        """Yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if object is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation of Rectangle obj attributes"""

        super().__init__() # Call to constructor  of the parent class
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
