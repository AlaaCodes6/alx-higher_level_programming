#!/usr/bin/python3
""" Module writes to a file
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file

    Args:
        filename: filename
        text: text to write
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
