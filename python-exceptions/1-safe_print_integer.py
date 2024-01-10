#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (isinstance(value, int)):
            int_value = int(value)
            print("{:d}".format(int_value))
            return True    
    except Exception:
        return False
