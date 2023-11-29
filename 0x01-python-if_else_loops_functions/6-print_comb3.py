#!/usr/bin/python3
for f in range(0, 8):
    for b in range(f + 1, 10):
        print("{:d}{:d}".format(f, b), end=", ")
print("{:d}{:d}".format(f + 1, b))
