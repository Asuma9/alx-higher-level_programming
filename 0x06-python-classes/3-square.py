#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """How to get area of a square using class Square"""

    def __init__(self, size=0):
        """mMethod to initialize object square"""
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("Size must be > 0")

    def area(self):
        """Method to calculate area of object"""
        return (self.__size ** 2)
