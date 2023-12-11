#!/usr/bin/python3
"""Creates a function class"""


def is_kind_of_class(obj, a_class):
    """Function to return True if obj is an instance or obj is an instance
    of class that inherited the specified class, otherwise  False.

    Parameters:
    - obj: object to be checked.
    - a_class: specified class

    Return:
    - True if obj is an instance of a_class or its subclass
    """
    return isinstance(obj, a_class)
