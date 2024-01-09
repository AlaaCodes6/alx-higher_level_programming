#!/usr/bin/python3
""" Module saves object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    using a JSON representation

    Args:
        my_obj: object
        filename: textfile name

    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
