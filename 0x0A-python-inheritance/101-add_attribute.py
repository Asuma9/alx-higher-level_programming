#!/usr/bin/python3
"""Defines a function to add an attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Adds an attribute to an obj if its possible
    :param obj: obj to which attribute should be added to
    :param attr_name: name of the attribute.
    :param attr_value: value of the attribute.
    """

    if hasattr(obj, "__dict__") or isinstance(obj, dict):
        """Checks for dict attribute or its instance b4 adding sn attribute"""
        obj.__setattr__(attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
