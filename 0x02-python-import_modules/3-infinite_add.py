#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0")
    for arg in range(2, argc):
        argv_int = int(sys.argv[arg])
        argv_int += argv_int
    print(argv_int)