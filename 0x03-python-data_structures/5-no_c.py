#!/usr/bin/env python3
def no_c(my_string):
    for i in my_string:
        res = my_string.replace('c', '').replace('C', '')
        return res
