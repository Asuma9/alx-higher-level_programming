#!/usr/bin/python3

def print_last_digit(number):
    """Function to print last digit of a number"""
    last_digit = number % 10
    print("{}".format(last_digit), end="")
    return last_digit
