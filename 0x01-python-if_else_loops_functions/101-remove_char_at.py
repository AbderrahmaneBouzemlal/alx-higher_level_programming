#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if n > len(str) - 1:
        return str
    if n >= 0:
        if str[n]:
            new_str = str[:n]
            if str[n + 1]:
                new_str += str[n+1:]
            else:
                new_str = str[:-1]
        else:
            ...
    return new_str
