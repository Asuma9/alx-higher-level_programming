#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a subclass of BaseGeometry class"""
    
    def __init__(self, width, height):
        """Instantiation of Rectangle obj attributes"""
    
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
