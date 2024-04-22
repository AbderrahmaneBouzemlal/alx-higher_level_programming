#!/usr/bin/python3
""" 10-main """
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":
    rect = Rectangle(3, 4)
    print(rect)
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
