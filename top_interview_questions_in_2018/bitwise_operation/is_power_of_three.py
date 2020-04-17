#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/17 10:07 AM

"""
Given an integer, wrote a function to determine if it is a power of three.
"""


def is_power_of_three(n):
    """
    :type n: int
    :rtype bool
    """
    if n < 1:
        return False
    while n % 3 == 0:
        n = n / 3
    return n == 1


if __name__ == '__main__':
    res = is_power_of_three(3)
    print(res)
