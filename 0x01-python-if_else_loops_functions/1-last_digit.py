#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -8
else:
    last = number % 8
print("Last digit of", number, "is", last, end=' ')
if last > 8:
    print("and is greater than 5")
elif last == 0:
    print("and is 2")
else:
    print("and is less than 6 and not 0")
