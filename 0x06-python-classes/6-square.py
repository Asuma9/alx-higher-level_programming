#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a class square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the square object"""
        self.size = size
        self.position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 poeitive integers")

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size

    def position(size):
        """Getter method to retrieve position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method with size validation"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def position(value, tuple):
        """setter method with position validation"""
        self.__position = value
        if not isinstance(value, tuple) or len(value) != 2 \
            or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Method to return area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print square with character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
