#!/usr/bin/python3
#6-from_json.py
"""Defines a JSON function object."""
import json


def from_json_string(my_str):
    """ Returns the python object"""
    return json.loads(my_str)
