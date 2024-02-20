#!/usr/bin/python3
"""Defines class student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Represents constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method class Dictionary """
        return self.__dict__.copy()
