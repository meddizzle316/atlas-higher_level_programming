#!/usr/bin/python3
import sys


def main(args):
    if len(args) == 0:
        print(".")
        sys.exit()
    print ("{} arguments".format(len(args)))
    for i in range(len(args)):
        print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main(sys.argv[1:])
