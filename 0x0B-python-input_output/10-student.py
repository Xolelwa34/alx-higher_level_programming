#!/usr/bin/python3
"""Defines student class."""


class Student:

    def __init__(self, first_name, last_name, age):
        """Represent constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to retrieves a dictionary representation of a
        Student instance"""
        
        if (isinstance(attrs, list) and
                all(isinstance(y, str) for y in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__
