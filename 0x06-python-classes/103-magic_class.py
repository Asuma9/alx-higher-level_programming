#!/usr/bin/python3
"""Defines MagicClass"""


import math


class MagicClass:
    """Creates class MagicClass to be disambled"""
    def __init__(self, radius=0):
        """Method to initialize object class"""
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """method to return area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Method to calculate perimeter of a circle"""
        return (2 * math.pi * self.__radius)
