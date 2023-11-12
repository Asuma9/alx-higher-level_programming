#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None

    max_value = my_list[0]
    for number in my_list[1:]:
        if number > max_value:
            max_value = number
    return (max_value)
