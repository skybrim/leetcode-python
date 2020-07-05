#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: single_numbers
@author: wiley
@datetime: 2020/7/5 9:08 PM

数组中只出现一次的数字
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是 O(n)，空间复杂度是 O(1)。
"""


def single_numbers(nums):
    """
    @param nums: List[int]
    @return: List[int]
    """
    ret = 0
    for num in nums:
        ret ^= num
    div = 1
    while div & ret == 0:
        div <<= 1
    res1 = 0
    res2 = 0
    for num in nums:
        if num & div:
            res1 ^= num
        else:
            res2 ^= num
    return [res1, res2]
