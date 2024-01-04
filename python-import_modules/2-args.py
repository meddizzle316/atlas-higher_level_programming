#!/usr/bin/python3
import sys


def main(argv):
    if len(argv) == 0:
        print(".")
        sys.exit()
    print ("{} arguments".format(len(argv)))
    for i in (len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main(sys.argv[1:])
