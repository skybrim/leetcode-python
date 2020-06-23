#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: count_digit_one.py
@author: wiley
@datetime: 2020/6/22 9:26 AM

1 ~ n 整数中 1 出现的次数
输入一个整数 n，求 1~n 这 n 个整数的十进制表示中 1 出现的次数。
例如：输入 12，1~12 中包含 1 的数字有 1、10、11、12，1 一共出现了 5 次
"""


def count_digit_one(n):
    if n <= 0:
        return 0
    high, cur, low = n // 10, n % 10, 0
    digit = 1
    result = 0
    while high != 0 or cur != 0:
        if cur == 0:
            result += high * digit
        elif cur == 1:
            result += high * digit + 1 + low
        else:
            result += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high = high // 10
        digit *= 10
    return result


if __name__ == '__main__':
    pass
