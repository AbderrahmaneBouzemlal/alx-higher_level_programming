#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square
if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    r3 = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89 })
    print(r1)
    print(r2)
    print(r3)
    print(r1 is r2)
    print(r1 == r2)
