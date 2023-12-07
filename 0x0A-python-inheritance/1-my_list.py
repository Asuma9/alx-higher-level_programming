#!/usr/bin/python3
"""Creates an inheritance class Mylist"""


class MyList(list):
    """Inherits from object list"""

    def print_sorted(self):
        """Prints the inherited list, sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
