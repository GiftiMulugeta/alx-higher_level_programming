#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = 1
    if isinstance(my_list, list):
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i - x]))
            x += 2
