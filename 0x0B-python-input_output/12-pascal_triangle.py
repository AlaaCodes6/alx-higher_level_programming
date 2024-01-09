#!/usr/bin/python3
"""Module Pascal's Triangle"""


def pascal_triangle(n):
    """A function that returnsa list of
    lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        j = triangle[-1]
        tmp = [1]
        for i in range(len(j) - 1):
            tmp.append(j[i] + j[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
