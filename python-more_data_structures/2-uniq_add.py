#!/usr/bin/python3
def uniq_add(my_list=[]):
    lowest_value = min(my_list)
    max = lowest_value
    total = lowest_value
    my_list.sort()
    for i in range(len(my_list)):
        if my_list[i] > max: 
            total += my_list[i]
            max = my_list[i]
    return total
