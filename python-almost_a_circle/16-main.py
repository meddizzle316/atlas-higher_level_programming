#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(5, 8, 1)
    r2 = Rectangle(9, 1, 3, 2)
    Rectangle.save_to_file([r1, r2])

    s1 = Square(2)
    s2 = Square(4, 1)
    Square.save_to_file([s1, s2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

    with open("Square.json", "r") as file:
        print(file.read())
