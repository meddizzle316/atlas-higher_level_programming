#!/usr/bin/python3
"""This is a basic module to help us learn about unit tests

"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
