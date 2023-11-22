#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
        return (output)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        output = None
    return (output)
