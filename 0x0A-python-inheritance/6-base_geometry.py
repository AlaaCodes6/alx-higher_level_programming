#!/usr/bin/python3
""" Raise exeption
"""


class BaseGeometry:
    """ empty class"""
    def area(self):
        raise Exception('area() is not implemented')
