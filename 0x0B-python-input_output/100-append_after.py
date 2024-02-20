#!/usr/bin/python3
"""Defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Method to insert a line of texts to a file"""

    Args:
        """filename (str, optional): name of file. Defaults to "".
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert."""
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
