#!/usr/bin/python3
import hidden_4


def main(args):
    list = dir(hidden_4)
    for i in list:
        if not i[0] == "_":
            print(list[i])


if __name__ == "__main__":
    main()
