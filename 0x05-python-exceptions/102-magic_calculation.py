#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    max_attempts = 3

    for attempt in range(0, max_attempts + 1):
        try:
            if attempt > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / attempt
        except Exception as e:
            print(f"Exception: {e}")
            result = b + a
            break
    else:
        print("No exception occurred during the loop.")

    return result
