#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_new = []
    for f in set_1:
        for b in set_2:
            if f == b:
                set_new.append(f)
    return set_new
