#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """

    Args:
        my_list (list): list to print from.
        x (int): number of elements of my_list to print.

    Returns:
        number of elements printed.

    """

    try:
        count = 0
        for element in my_list[:x]:
            if count == x:
                break
            if type(element) == int:
                print("{:d}".format(element), end='')
                count += 1
        print()
        return count
    except (TypeError, IndexError):
        print()
        raise
