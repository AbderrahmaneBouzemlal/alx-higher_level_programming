#!/usr/bin/python3
import sys
argc = len(sys.argv)
argc -= 1
if argc == 0:
    print(f"{argc} arguments.")
elif argc == 1:
    print(f"{argc} argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{argc} arguments:")
    for i in range(1, argc + 1):
        print(f"{i}: {sys.argv[i]}")
