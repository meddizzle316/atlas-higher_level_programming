#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print (number % 10, end="")
        return (number % 10)
    elif number < 0:
        print ((abs(number) % 10) * -1, end="")
        return((abs(number) % 10) * -1)
