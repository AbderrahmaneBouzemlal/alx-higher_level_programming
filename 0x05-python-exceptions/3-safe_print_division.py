#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
        return result
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(result))

