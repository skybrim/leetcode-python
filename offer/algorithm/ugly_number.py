#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: ugly_number.py
@author: wiley
@datetime: 2020/6/24 10:00 AM

丑数
我们把只包含因子 2、3、5 的数称作丑数（Ugly Number）。
求按从小到大的顺序的第 1500 个丑数。
习惯上我们把 1 当做第一个丑数。
"""


def get_ugly_number(n):
    """
    @param n: int
    @return: int
    """
    if n <= 0:
        return 0
    store = {1: 1}
    last = 1
    t2 = 1
    t3 = 1
    t5 = 1
    while last < n:
        last_number = min(store[t2] * 2, store[t3] * 3, store[t5] * 5)
        last += 1
        store[last] = last_number

        while store[t2] * 2 <= store[last]:
            t2 += 1
        while store[t3] * 3 <= store[last]:
            t3 += 1
        while store[t5] * 5 <= store[last]:
            t5 += 1
    print(store)
    return store[n]


if __name__ == '__main__':
    result = get_ugly_number(11)
    print(result)
