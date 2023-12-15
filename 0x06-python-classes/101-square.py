#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Creates a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size manipulation with value validation"""
        if not isinstance(value, int):
            raise Exception("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position value manipulation with validation"""
        if not isinstance(value, tuple) or len(value) != 2\
            or not all(isinstance(i, int) for i in value)\
                or any(i < 0 for i in value):
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to get area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square to stdout with character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    def __str__(self):
        """string representation of the square"""
        result = ""
        if self.size == 0:
           result += "\n"
        else:
            for _ in range(self.position[1]):
                result += "\n"
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip()
