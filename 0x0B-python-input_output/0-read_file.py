#!/usr/bin/python3
"""Defines a textfile for reading function."""

def read_file(filename=""):
    """Module contents of UTF8 text file to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
