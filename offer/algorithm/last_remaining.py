#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: last_remaining.py
@author: wiley
@datetime: 2020/7/15 11:03 AM

圆圈中最后剩下的数字
0, 1, ..., n-1, 这 n 个数字排成一个圆圈，从数字 0 开始，每次从这个圆圈里删除第 m 个数字。
求出这个圆圈里剩下的最后一个数字。

举例：
0， 1， 2， 3， 4 这 5 个数字，组成一个圆圈，从数字 0 开始每次删除第 3 个数字；
则删除的前 4 个数字一次是 2，0，4，1，因此最后剩下的数字是 3。
"""


def last_remaining(n, m):
    """
    @param n: int
    @param m: int
    @return: int
    """
    point = 0
    nums = list(range(n))
    while len(nums) > 1:
        for _ in range(m - 1):
            point += 1
            if point == len(nums):
                point = 0
        nums.pop(point)
        if point >= len(nums):
            point = 0
    return nums[0]


def last_remaining_ii(n, m):
    if n < 1 or m < 1:
        return -1
    result = 0
    for i in range(2, n + 1):
        result = (result + m) % i
    return result


if __name__ == '__main__':
    res = last_remaining(5, 3)
    print(res)
