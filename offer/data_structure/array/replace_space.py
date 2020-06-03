#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: replace_space.py
@author: wiley
@datetime: 2020/5/13 9:47 AM

替换空格
实现一个函数，把字符串 s 中的每个空格，替换成“%20”
"""


def replace_space(s):
    """
    :param s: str
    :return: str
    """
    res = []
    for c in s:
        if c == " ":
            res.append("%20")
        else:
            res.append(c)
    return "".join(res)


if __name__ == '__main__':
    temp = replace_space("We are happy.")
    print(temp)
