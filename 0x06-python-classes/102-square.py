#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Creates a class Square"""
    def __init__(self, size=0):
        """Method to initialize object square"""
        self.size = size

    @property
    def size(size):
        """Getter method to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size with validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to return area of a square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparator based on square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator based on square area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator base on square area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on square area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator based on square area"""
        return self.area() < other.area()

    def __le__self(self, other):
        """Less than or equal comparator based on square area"""
        return self.area() <= other.area()
