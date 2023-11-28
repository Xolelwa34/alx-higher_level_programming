#!/usr/bin/python3
for char in range(0, 8):
    for b in range(char + 1, 10):
        print("{:d}{:d}".format(char, b), end=", ")
print("{:d}{:d}".format(char + 1, b))
