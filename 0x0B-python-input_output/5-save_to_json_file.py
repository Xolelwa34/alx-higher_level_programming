#!/usr/bin/python3
"""Defins a function that saves a file."""
#5-save_to_json_file.py
import json


def save_to_json_file(my_obj, filename):
    """Method to writes an Object to a text file, using a JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
