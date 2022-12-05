#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #x = 1
    #for i in range(len(my_list)):
        #print("{:d}".format(my_list[i - x]))
        #x += 2
    for i in range(-1, -len(my_list) - 1, -1):
        print("{:d}".format(my_list[i]))
