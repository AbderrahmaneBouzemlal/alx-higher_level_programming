#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, a + b))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, a - b))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, a * b))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, a / b))
