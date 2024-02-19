#!usr/bin/python3
"""Defines an object attribute function lookup"""


def lookup(obj):
    """Returns the available list of objects attributes."""
    return (dir(obj))
