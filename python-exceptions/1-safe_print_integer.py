#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True    
    except Exception:
        return False
