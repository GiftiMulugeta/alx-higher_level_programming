#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        length = len(str)
        if (n > length or n < 0):
            print("{}".format(i), end="")
        else:
            if (i == str[n]):
                continue
            print("{}".format(i), end="")
