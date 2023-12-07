#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for c, count in sorted(a_dictionary.items()):
        print("{}: {}".format(c, count))
