#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: first_uniq_char.py
@author: wiley
@datetime: 2020/6/28 10:58 AM

第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
s 只包含小写字母。
"""


def first_uniq_char(s):
    """
    @param s: str
    @return: str
    """
    store = {}
    for char in s:
        if char in store:
            store[char] = False
        else:
            store[char] = True
    for char in s:
        if store[char]:
            return char
    return " "


if __name__ == '__main__':
    result = first_uniq_char("abaccdeff")
    print(result)

