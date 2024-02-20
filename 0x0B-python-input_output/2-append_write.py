#!/usr/bin/python3
"""Defines file appending."""

def append_write(filename="", text=""):
    """Append a string to the end of text-file."""

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
