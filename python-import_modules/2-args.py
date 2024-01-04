#!/usr/bin/python3
import sys


def main(argv):
    if len(argv) == 1:
        print(".")
        sys.exit()
    print ("{} arguments".format(len(argv) - 1))
    for i in (len(argv) - 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
