#!/usr/bin/python3
"""Defines a python class to JSON."""

def class_to_json(obj):
    """Method to the dictionary"""
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
