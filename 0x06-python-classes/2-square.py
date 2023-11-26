#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Class that defines a square with size validation"""

    def __init___(self, size=0):
        """Method that initializes a square object"""
        self.__size = size

        if not isinstance(_size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
	    self.__size = int(size)
