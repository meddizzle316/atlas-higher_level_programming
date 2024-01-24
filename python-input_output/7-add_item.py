#!/usr/bin/python3
"""
a script that adds all arguments to a
Python list, and then save them
to a file
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
arg = sys.argv[1:]
with open('add_items.json', 'w') as file:
    for i in arg:
        save_to_json_file(i, file)
        print(i)
    load_from_json_file(file)
