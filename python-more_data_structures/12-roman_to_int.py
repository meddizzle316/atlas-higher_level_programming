#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V':5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        s = roman_string[i]
        try:
            n = roman_string[i + 1]
            if s in dict and n in dict and dict[s] < dict[n]:
                result -= dict[s]
            elif s in dict:
                result += dict[s]
        except IndexError:
            if s in dict:
                result += dict[s]
    return result
