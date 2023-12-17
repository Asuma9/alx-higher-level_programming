#!/usr/bin/python3
"""Print a string in uppercase"""

def uppercase(str):
    """Method/function to print a string in uppercase"""
    for c in str:
        if 97 <= ord(c) <= 122:  #  check if it is a lower case
            c = chr(ord(c) - 32)  #  Convert it to uppercase
        print("{}".format(c), end="")
    print("")
