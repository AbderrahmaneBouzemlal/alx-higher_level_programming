#!/usr/bin/python3
for i in range(26, 0, -1):
    if i % 2 != 0:
        print("{:c}".format(i + 64), end="")
    else:
        print("{:c}".format(i + 96), end="")
