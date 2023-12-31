#!/usr/bin/python3
"""

Module composed by a function that prints 2 new lines after some characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for j in ".?:":
        list_text = s.split(j)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + j if s is "" else s + "\n\n" + i + j

    print(s[:-3], end="")
