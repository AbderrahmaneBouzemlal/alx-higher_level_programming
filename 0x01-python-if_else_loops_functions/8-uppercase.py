#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c > 96 or c > 97 + 26:
            c -= 32
        c = chr(c)
        print("{}".format(c), end="")
    print("")
