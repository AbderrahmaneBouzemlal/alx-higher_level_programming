#!/usr/bin/python3
# base.py
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to save a list of classes as json"""
        list_dict = []
        if list_objs is not None and type(list_objs) is list:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """return a list from a json string"""
        list_json = []
        if json_string is None or json_string == "":
            return list_json
        list_json = json.loads(json_string)
        return list_json

    @classmethod
    def create(cls, **dictionary):
        """Return a class instant from a dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                rects = []
                data = file.read()
                dictionary = cls.from_json_string(data)
                for i in dictionary:
                    rects.append(cls.create(**i))
                return rects
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """converts the list of objects to a csv file"""
        with open(f"{cls.__name__}.csv", "w") as csvfile:
            fieldnames = []
            list_dict = []
            if list_objs is not None and type(list_objs) is list:
                for obj in list_objs:
                    dic = obj.to_dictionary()
                    for k, v in dic.items():
                        if k in fieldnames:
                            continue
                        fieldnames.append(k)
                    list_dict.append(dic)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """extracting data from a csv file"""
        ls_csv = []
        d = {}
        with open(f"{cls.__name__}.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for k, v in row.items():
                    d[k] = int(v)
                ls_csv.append(cls.create(**d))
        return ls_csv
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#60CE80")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
