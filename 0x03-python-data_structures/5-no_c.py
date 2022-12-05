#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new = new + my_string[i]
    return new
