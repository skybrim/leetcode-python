#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: my_pow.py
@author: wiley
@datetime: 2020/5/19 10:39 AM

实现 pow(x, n)，即计算 x 的 n 次幂函数
"""


def my_pow(x, n):
    """
    @param x: float
    @param n: int
    @return: float
    """
    if n == 0 or x == 1:
        return 1
    if n == 1:
        return x
    if n < 0:
        x, n = 1 / x, -n
    result = my_pow(x, n >> 1)
    result *= result
    if n & 1 == 1:
        result *= x
    return result


def my_pow_s(x, n):
    """
    @param x: float
    @param n: int
    @return: float
    """
    if n == 0 or x == 1:
        return 1
    if n == 1:
        return x
    res = 1
    if n < 0:
        x, n = 1 / x, -n
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


if __name__ == '__main__':
    pass
