#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if not i == x and x > i and i < 8:
            print("{}{}".format(i, x), end=", ")
        elif not i == x and x > i and i == 8:
            print("{}{}".format(i, x))
