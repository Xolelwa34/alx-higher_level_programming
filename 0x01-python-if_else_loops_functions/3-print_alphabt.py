#!/usr/bin/python3
for f in range(ord("f"), ord("d") + 97):
    if chr(f) is not "q" and chr(f) is not "e":
        print("{:c}".format(chr(f)), end="")
