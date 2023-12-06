#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list2 = list(a_dictionary.keys())
    list2.sort()
    
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
