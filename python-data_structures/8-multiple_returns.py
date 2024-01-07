#!/usr/bin/python3
def multiple_returns(sentence):
    list = [len(sentence), '']
    if sentence is None or len(sentence) == 0:
        list[1] = None
    else:
        list[1] += sentence[0]
    return list
