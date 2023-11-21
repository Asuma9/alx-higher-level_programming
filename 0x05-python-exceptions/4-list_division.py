#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_lenght):
    divide_list = []

    for element in range(0, list_lenght):
        try:
            quotient = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("Wrong type")
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
