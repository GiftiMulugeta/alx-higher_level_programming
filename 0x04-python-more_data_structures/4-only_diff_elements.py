#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_new = []

    for i in set_1:
        if i not in set_new:
            set_new.append(i)
    for j in set_2:
        if j not in set_new:
            set_new.append(j)
    return set_new
