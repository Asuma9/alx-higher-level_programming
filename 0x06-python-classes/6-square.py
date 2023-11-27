#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a class square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size

    @property
    def position(size):
        """Getter method to retrieve position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method with size validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter method with position validation"""
        if not isinstance(value, tuple) or len(value) != 2 \
            or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to return area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print square with character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
