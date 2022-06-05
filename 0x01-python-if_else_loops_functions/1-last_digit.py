#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberlas = int(repr(number)[-1])
numberlass = number * -1
str = " "
if numberlass <= 0:
    if numberlas > 5:
        str = "and is greater than 5"
    elif numberlas == 0:
        str = "and is 0"
    elif numberlas < 6 and numberlas != 0:
        str = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {numberlas} {str}")
elif numberlass > 0:
    numberlas = -1 * int(repr(number)[-1])
    if numberlas > 5:
        str = "and is greater than 5"
    elif numberlas == 0:
        str = "and is 0"
    elif numberlas < 6 and numberlas != 0:
        str = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {numberlas} {str}")
