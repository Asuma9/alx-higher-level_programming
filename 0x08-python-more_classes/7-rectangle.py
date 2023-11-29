#!/usr/bin/python3
"""Creates class Rectangle"""


class Rectangle:
    """Defines class Rectangle"""

    number_of_instances = 0   # class attribute
    print_symbol = '#'  # public class attribute for print symbol

    def __init__(self, width=0, height=0):
        """Method to initialize the object Rectangle with attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter to retrieve rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width with validation tests"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter method to retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation tests"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        """Method to return perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height) * 2

    def area(self):
        """Method to return area of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def __str__(self):
        """Method to print a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (f'{str(self.print_symbol)*self.width}\n'*self.height).\
            strip("\n")

    def __repr__(self):
        """Method to print string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method to delete and track instances deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
