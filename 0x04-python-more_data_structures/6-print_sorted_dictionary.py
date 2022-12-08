#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary)
    for key in sorted_key:
        print(key + ": ", end="")
        print(a_dictionary[key])
