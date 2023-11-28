#!/usr/bin/python3
for char in range(ord("char"), ord("d") + 1):
    if chr(char) is not "q" and chr(char) is not "e":
        print("{:c}".format(chr(char)), end="")
