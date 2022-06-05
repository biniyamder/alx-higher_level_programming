#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberlas = int(repr(number)[-1])
str = " "
if numberlas > 5:
    str = "and is greater than 5"
elif numberlas == 0:
    str = "and is 0"
elif numberlas < 5:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {numberlas} {str}")
