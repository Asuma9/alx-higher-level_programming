#!/usr/bin/python3
"""Creates an object"""


def is_same_class(obj, a_class):
    """Function to check if object is an exact instance of stated class"""
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
