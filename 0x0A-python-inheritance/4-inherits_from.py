#!/usr/bin/python3
"""Creates a function class"""


def inherits_from(obj, a_class):
    """Function to return True if obj is an instance of a class that
    inherited(directly/indirectly) from the specified class,
    otherwise return False.
    """
    return isinstance(obj, a_class) and issubclass(type(obj), a_class)\
        and type(obj) is not a_class
