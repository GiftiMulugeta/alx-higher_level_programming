#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    copy_list = my_list
    if idx < 0 or idx >= len(my_list):
        return copy_list
    else:
        my_list.remove(idx + 1)
    return my_list
