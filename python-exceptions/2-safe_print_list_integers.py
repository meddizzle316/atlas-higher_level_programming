#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0 
    try:
        for i in range(x):
            if type(my_list[i]) is type(i):
                print("{:d}".format(my_list[i]), end="")
                result += 1
        print()
    except Exception:
        print()
        return (result)
    else:
        return (result)
