#!/usr/bin/python3
"""Defines a module and classes to inherit"""


class BaseGeometry:
    """Parent class"""
    def area(self):
        """area object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be gretaer tha 0".format(name))


class Rectangle(BaseGeometry):
    """creates class Rectangle to inherit from BaseGeometry"""
    def __init__(self, width, height):
        """Method to initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Implement area"""
        return self.__width * self.__height

    def __str__(self):
        """Prints object attributes"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """subclass of Rectangle"""
    def __init__(self, size):
        """Instance of class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Customize area method for the square"""
        return self.__size * self.__size

    def __str__(self):
        """Prints Square attributes"""
        return "[Square] {}/{}".format(self.__size, self.__size)
