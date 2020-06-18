#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: get_least_numbers.py
@author: wiley
@datetime: 2020/6/18 9:55 AM

最小的 k 个整数
输入 n 个整数，找出其中最小的 k 个数。
例如，输入【4，5，1，6，2，7，3，8】，则最小的 4 个数字是 1、2、3、4
"""


def get_least_numbers(arr, k):
    """
    @param arr: List[int]
    @param k: int
    @return: List[int]
    """
    arr.sort()
    return arr[:k]


if __name__ == '__main__':
    temp = get_least_numbers([0,1,1,2,4,4,1,3,3,2], 6)
    print(temp)
