#!/usr/bin/python3
for a in range(0, 26):
    if a == 4 or a == 16:
        continue
    print(chr(a + 97), end="")
