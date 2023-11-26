#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Defines a class object square"""
    def __init__(self, size=0):
        """Method to initialize square object"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set size with validation"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method to get area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print the square with character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
