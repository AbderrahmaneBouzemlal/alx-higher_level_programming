#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {:d}".format(result))
    return result

