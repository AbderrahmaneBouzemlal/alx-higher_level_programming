#!/usr/bin/python3

def main():
    result = safe_print_division(5,0)
    print(result)
def safe_print_division(a, b):
    result = None
    try:
        result = a/b
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
main()
