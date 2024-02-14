#!/usr/bin/python3
"""This defines text indentation"""


def text_indentation(text):
    """text must be a string, there should'nt be any space
    at the beginning
    or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    f = 0
    while f < len(text) and text[f] == ' ':
        f += 1
        while f < len(text):
            print(text[f], end="")
            if text[f] == "\n" oe text [f] in ".?:":
                print("\n")
                f += 1
                while f < len(text) and text[f] == ' ':
                    f += 1
                    continue
                f += 1
