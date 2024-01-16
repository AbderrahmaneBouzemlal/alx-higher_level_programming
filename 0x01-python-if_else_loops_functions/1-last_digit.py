#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print(f"Last digit of {number}", end=" ")
if number > 5:
    print(f"is {last_digit} and is greater than 5")
elif number == 0:
    print(f"is {last_digit} and is 0")
else:
    if number < 0:
        last_digit = number % -10
        print(f"is {last_digit} and is less than 6 and not 0")
