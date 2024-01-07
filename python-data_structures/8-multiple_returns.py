#!/usr/bin/python3
def multiple_returns(sentence):
    list = []
    list[0] = len(sentence)
    if sentence is None:
        list[0] = None
    list[1] = sentence[0]
    return list
