#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list = []
    stored_tuple = (0, 0)
    if len(tuple_a) < 2:
        tuple_a += stored_tuple
    if len(tuple_b) < 2:
        tuple_b += stored_tuple
    for i in range(2):
        if tuple_a[i] is None:
            pass 
        else: 
            a = tuple_a[i]
        if tuple_b[i] is None:
            pass
        else:
            b = tuple_b[i]
        total = a + b
        new_list.append((total)) 
    return tuple(new_list)
