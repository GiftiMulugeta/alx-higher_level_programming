#!/usr/bin/env python3
def no_c(my_string):
    #new = ""
    #for i in range(len(my_string)):
     #   if my_string[i] == 'c' or my_string[i] == 'C':
    #        continue
   # else:
     #   new = new + my_string[i]
    #return new
    copy = [x for x in my_string if x!= 'c' and x != 'C']
    return("".join(copy))
