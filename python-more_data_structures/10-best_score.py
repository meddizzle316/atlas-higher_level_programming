#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    values_list = list(a_dictionary.values())
    max = -922337203685477
    for i in range(len(values_list)):
        if values_list[i] > max:
            max = values_list[i]
    if max == -922337203685477:
        return None
    for key, value in a_dictionary.items():
        if value == max:
            return key
    return None
