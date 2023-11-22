#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ Divides elementwise between two list

    Args:
        my_list_1(list): the first list
        my_list_2(list): the second list
        list_lenght(int): number of elemnts to divide

    Returns:
        A new list of lenght list_lenght containg all the divisions

    """

    divide_list = []
    for element in range(0, list_length):
        try:
            quotient = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            divide_list.append(quotient)
    return divide_list
