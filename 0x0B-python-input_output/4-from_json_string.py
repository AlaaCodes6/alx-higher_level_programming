#!/usr/bin/python3
""" Module from JSON to string
"""
import json


def from_json_string(my_str):
    """ Function that returns an object represented by JSON

    Args:
        my_str: JSON representation string

    """
    return json.loads(my_str)
