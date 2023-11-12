#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    multiples_2_list = []
    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            multiples_2_list.append(True)
        else:
            multiples_2_list.append(False)
    return multiples_2_list
