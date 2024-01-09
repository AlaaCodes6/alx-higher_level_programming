#!/usr/bin/python3
""" Module class to JSON
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description with a simple
data structure for a JSON serialization of an object
"""

    data_st = {}
    if hasattr(obj, "__dict__"):
        data_st = obj.__dict__.copy()
    return data_st
