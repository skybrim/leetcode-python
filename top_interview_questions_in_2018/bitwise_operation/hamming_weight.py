#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/14 10:14 AM

"""
Write a function that takes an unsigned integer and
return the number of '1' bits it has (also known as the hamming weight).
"""


def hamming_weight(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    while n > 0:
        result += n & 1
        n >>= 1
    return result


if __name__ == '__main__':
    res = hamming_weight(10)
    print(str(res))
