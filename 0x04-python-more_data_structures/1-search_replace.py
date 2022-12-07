#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list.copy()
    for i, item in enumerate(copy_list):
        if item == search:
            copy_list[i] = replace
    return copy_list
