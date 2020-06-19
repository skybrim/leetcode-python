#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: max_sub_array.py
@author: wiley
@datetime: 2020/6/19 9:17 AM

连续子数组的最大和
输入一个整型数组，数组里有正数也有复数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。
"""


def max_sub_array(nums):
    """
    @param nums: List[int]
    @return: int
    """
    res = nums[0]
    cur = nums[0]
    for i in range(1, len(nums)):
        if cur < 0 and nums[i] > 0:
            cur = nums[i]
        else:
            cur += nums[i]
        res = max(cur, res)
    return res


if __name__ == '__main__':
    temp = max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    print(temp)
