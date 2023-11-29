#!/usr/bin/python3
for f in reversed(range(ord("f"), ord("z") + 1)):
    if f % 2 != 0:
        f =f - 32
    print("{:c}".format(f), end="")
