#!/usr/bin/python3
"""Creates class Rectangle"""


class Rectangle:
    """Defines class Rectangle"""

    number_of_instances = 0   # class attribute
    print_symbol = '#'  # public class of print symbol

    def __init__(self, width=0, height=0):
        """Method to initialize object rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter to return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method with width validation"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter method for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method with height validation"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        """Method to get perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * self.height) * 2

    def area(self):
        """Method to get area of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def __str__(self):
        """Method to print the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (f'{str(self.print_symbol) * self.width}\n' * self.height).\
            strip("\n")

    def __repr__(self):
        """Method for string representantion of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method to delete and track deleted instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to compare the area of rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2
