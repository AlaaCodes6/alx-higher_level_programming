#!/usr/bin/python3
""" Module read file"""


def read_file(filename=""):
    """ Function that reads a text file

    Args:
        filename: filename

    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end='')
