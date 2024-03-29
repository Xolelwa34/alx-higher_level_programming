#!/usr/bin/python3
"""Defines a Base class."""
from json import dumps, loads
import csv


class Base:
    """Represents the base of our OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps.json(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Unjsonifies is a dictionary."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save jsonified object to file."""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """Method to load a string from file and unjsonifies"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Method instance from dictionary."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method to save object to csv file."""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writelines(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Method to load object to csv file."""
        from models.rectangle import Rectangle
        from models.square import Square
        get = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                line = [int(l) for r in line]
                if cls is Rectangle:
                    d = {"id": line[0], "width": line[1], "height": line[2],
                         "x": line[3], "y": line[4]}
                else:
                    d = {"id": line[0], "size": line[1],
                         "x": line[2], "y": line[3]}
                get.append(cls.create(**d))
        return get

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import tyme
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            tur = turtle.Turtle()
            tur.color((randrange(255), randrange(255), randrange(255)))
            tur.pensize(1)
            tur.penup()
            tur.pendown()
            tur.setpos((i.x + tur.pos()[0], i.y - tur.pos()[1]))
            tur.pensize(10)
            tur.forward(i.width)
            tur.left(90)
            tur.forward(i.height)
            tur.left(90)
            tur.forward(i.width)
            tur.left(90)
            tur.forward(i.height)
            tur.left(90)
            tur.end_fill()

        tyme.sleep(5)
