#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """function that removes all characters c and C from a string."""
    less_string = ""
    for item in my_string:
        if item == "c" or item == "C":
            continue
        less_string += item
    return less_string
