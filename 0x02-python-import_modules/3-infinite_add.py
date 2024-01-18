#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0   
    argc = len(sys.argv)
    for arg in range(1, argc):
        sum += int(sys.argv[arg])
    print(sum)
