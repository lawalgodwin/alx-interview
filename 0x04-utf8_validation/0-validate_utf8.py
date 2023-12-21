#!/usr/bin/python3
"""A module containing a utf8 data set validator"""


def validUTF8(data):
    """ A utf8 validation function """
    return all([d <= 255 for d in data])
