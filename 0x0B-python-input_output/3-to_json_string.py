#!/usr/bin/python3
"""Defines a string to JSON funct."""
import json


def to_json_string(my_obj):
    """Method to return the JSON representation of a string object"""
    return json.dumps(my_obj)
