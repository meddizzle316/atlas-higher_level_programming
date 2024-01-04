#!/usr/bin/python3
def uppercase(str):
    str = str + '\n'
    for i in range(len(str)): 
        ascii_value = ord(str[i])
        if ascii_value > 96 and ascii_value < 123:
            print("{}".format(chr(ascii_value - 32)), end="")
        else:
            print(str[i], end="")
