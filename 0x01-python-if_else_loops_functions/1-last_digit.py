#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
num_str = repr(number)
repr_num = num_str[-1]
git = int(repr_num)
sign = '-'
if git > 5:
    print(f"Last digit of {number} is {git} and is greater than 5")
if git == 0:
    print(f"Last digit of {number} is {git} and is 0")
if git < 6 and git != 0 and number < 0:
    print(f"Last digit of {number} is {sign}{git} and is less than 6 and not 0")
if git < 6 and git != 0 and number > 0:
    print(f"Last digit of {number} is {git} and is less than 6 and not 0")
