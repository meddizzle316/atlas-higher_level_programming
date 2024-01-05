#!/usr/bin/python3
import sys


def main(args):
    result = 0
    if args == 0:
        print("0")
        sys.exit()
    for i in range(len(args)):
        print(args[i], i)
        result += int(args[i])
    print (result)


if __name__ == "__main__":
    main(sys.argv[1:])
