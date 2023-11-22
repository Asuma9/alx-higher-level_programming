#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = (a ** 2) * (b * 5)
    return result

#Display the bytecode of the function
dis.dis(magic_calculation)
