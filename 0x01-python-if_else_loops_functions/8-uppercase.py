#!/usr/bin/python3

def uppercase(str):
    """Method/function to print a string in uppercase"""
    for c in str:
        if 'a' <= c <= 'z':
            uppercase_char = chr(ord(c) - ord('a') + ord('A'))
        else:
            uppercase_char = c
        print("{}".format(uppercase_char), end="")
    print("")
