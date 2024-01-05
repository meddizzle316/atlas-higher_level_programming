#!/usr/bin/python3
import sys


def main(args):
    if len(args) == 0:
        print("{} arguments.".format(len(args)))
        sys.exit()
    elif len(args) == 1:
        print("{} argument:".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
    for i in range(0, len(args)):
        print("{}: {}".format(i + 1, args[i]))


if __name__ == "__main__":
    main(sys.argv[1:])
