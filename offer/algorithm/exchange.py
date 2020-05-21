#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: exchange.py
@author: wiley
@datetime: 2020/5/21 10:57 AM

调整数组顺序使奇数位于偶数前面。
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，是得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""


def exchange(nums):
    """
    @param nums: List[int]
    @return: List[int]
    """
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] & 1 == 1:
            i += 1
        while i < j and nums[j] & 1 != 1:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == '__main__':
    pass
