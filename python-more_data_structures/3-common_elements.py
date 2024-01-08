#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1_list = list(set_1)
    set_2_list = list(set_2)
    new_set = set()
    for i in range(len(set_1_list)):
        for x in range(len(set_2_list)):
            if set_1_list[i] == set_2_list[x]:
                new_set.add(set_1_list[i])
    return new_set
