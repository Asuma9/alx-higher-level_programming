#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class to define a square with private attribures"""
    def __init__(self, size=0):
        """Method to initialize the object square"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """Method to find area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size with validation"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
