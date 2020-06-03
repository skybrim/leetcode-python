#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: hamming_weight.py
@author: wiley
@datetime: 2020/5/19 10:01 AM

二进制中 1 的个数 （汉明重量）
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
"""


def hamming_weight(n):
    """
    @param n: int
    @return: int
    """
    result = 0
    while n:
        result += n & 1
        n >>= 1
    return result


if __name__ == '__main__':
    pass
