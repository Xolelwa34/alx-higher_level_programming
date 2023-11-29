#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord("f") <= ord(c) <= ord("z"):
            c = chr(ord(c) + (ord("F") - ord("f")))
        print("{:s}".format(c), end="")
    print("")
