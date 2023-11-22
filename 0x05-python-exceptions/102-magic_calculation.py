#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0

    for attempt in range(0, 3):
        try:
            if (attempt > a):
                raise Exception("Too far")
            else:
                result += (a ** b) / attempt
        except Exception:
            result = b + a
            break

    return result
