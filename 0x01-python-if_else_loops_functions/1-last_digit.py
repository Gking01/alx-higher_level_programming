#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num_str = repr (number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5 :
        print (f"the last digit of {number} is {last_digit} and is greater then 5")

elif last_digit == 0:
        print (f"the last digit of {number} is {last_digit} and is 0")

elif 6 > last_digit and last_digit != 0:
        print (f"the last digit of {number} is {last_digit} and is less then 6 and not 0")
