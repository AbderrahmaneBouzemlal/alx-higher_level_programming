#!/usr/bin/python3
def roman_to_int(roman_number):
    roman = {
        "I": 1,
        "V": 5,    
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500
    }
    if not roman_number:
        return None
    if str(roman_number).isdigit():
        return None
    number = 0
    for i in range(len(roman_number)-1):
        if roman[roman_number[i]] < roman[roman_number[(i+1)]]:
            number-=roman[roman_number[i]]
        else:
            number+=roman[roman_number[i]]
    return number+roman[roman_number[-1]]
