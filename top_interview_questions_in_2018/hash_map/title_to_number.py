#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: title_to_number.py
@author: wiley
@datetime: 2020/5/8 9:21 AM

Given a column title as appear in an Excel sheet, return its corresponding column number.
"""


def title_to_number(s):
    """
    :param s: str
    :return: int
    """
    res = 0
    difference = ord('A') - 1
    i = 0
    for char in s[::-1]:
        res += (ord(char) - difference) * (26 ** i)
        i += 1
    return res


if __name__ == '__main__':
    temp = title_to_number('ZY')
    print(str(temp))