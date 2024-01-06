#!/usr/bin/python3
"""

This module is composed by a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Args:
        matrix: list of a lists of integers or floats
        div: number that divides the matrix

    Returns:
        A new matrix

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If division is zero


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg1)

    len_e = 0
    msg2 = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg1)

        if len_e != 0 and len(elements) != len_e:
            raise TypeError(msg2)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msg1)

        len_e = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
