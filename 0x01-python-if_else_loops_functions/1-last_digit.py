#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = 0
if number < 0:
    number *= -1
    num1 = 1
last_digit = number % 10
if num1 == 1:
    number *= -1
    last_digit *= -1
print("Last digit of {} is ".format(number), end="")
if last_digit > 5:
    print("{}  and is greater than 5".format(last_digit))
elif last_digit == 0:
    print("{} and is 0".format(last_digit))
else:
    print("{} and is less than 6 and not 0".format(last_digit))
