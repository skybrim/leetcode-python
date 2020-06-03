#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: fib.py
@author: wiley
@datetime: 2020/5/18 10:57 AM

斐波那契数列
写一个函数，输入 n，求斐波那契（Fibonacci） 数列的第 n 项。
斐波那契数列的定义如下：
F(0) = 0, F(1) = 1,
F(N) = F(N-1) + F(N-2) 其中 N>1
"""


def fib(n):
    """
    @param n: int
    @return: int
    """
    if n < 2:
        return n
    one, two = 0, 1
    for _ in range(n):
        one, two = two, one + two
    return one % 1000000007


if __name__ == '__main__':
    pass
