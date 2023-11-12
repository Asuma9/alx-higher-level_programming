#!/usr/bin/python3
# 6-print_matrix_integer.py


def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples."""
    # handle tuple_a
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
        elif len(tuple_a) == 0:
            tuple_a = (0, 0)

        # Handle tuple_b
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        elif len(tuple_b) == 0:
            tuple_b = (0, 0)

        # tuple addition
        tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return (tuple_sum)
