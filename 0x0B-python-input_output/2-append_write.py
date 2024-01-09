#!/usr/bin/python3
""" Module append to a file
"""


def append_write(filename="", text=""):
    """ Function that appends a string to a text file

    Args:
        filename: filename
        text: text to write

    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
