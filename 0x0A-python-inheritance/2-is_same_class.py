#!/usr/bin/python3
"""Creates an object"""


def is_same_class(obj, a_class):
    """Function that returns True if obj is exactly an instance
    of the stated class, otherwise return False"""
    return type(obj) is a_class
