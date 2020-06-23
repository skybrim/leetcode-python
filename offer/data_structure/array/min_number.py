#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: min_number.py
@author: wiley
@datetime: 2020/6/23 9:15 AM

把数组排成最小的数
输入一个非负的整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
"""


import functools


def min_number(nums):
    """
    @param nums: List[int]
    @return: str
    """
    def help_sort(x, y):
        a, b = x + y, y + x
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    strings = [str(num) for num in nums]
    strings.sort(key=functools.cmp_to_key(help_sort))
    return ''.join(strings)


if __name__ == '__main__':
    result = min_number([1, 2, 3, 4])
    print(result)
