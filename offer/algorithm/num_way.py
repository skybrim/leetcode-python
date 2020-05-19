#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: num_way.py
@author: wiley
@datetime: 2020/5/19 9:39 AM

一直青蛙一次可以跳上 1 级台阶，也可以跳上 2 级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""


def num_way(n):
    """
    @param n: int
    @return: int
    """
    one, two = 1, 1
    for _ in range(n):
        one, two = two, one + two
    return one % 1000000007


if __name__ == '__main__':
    pass
