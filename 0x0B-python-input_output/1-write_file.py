#!/usr/bin/python3
"""Method of a file-writing function."""

def write_file(filename="", text=""):
    """ function that writes a str to a text file (UTF8) """

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
