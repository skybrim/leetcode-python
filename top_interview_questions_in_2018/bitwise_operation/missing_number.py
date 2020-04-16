#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/16 9:28 AM

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.
"""


def missing_number(nums):
    """
    :type nums: List(int)
    :rtype int
    """
    nums_sum = sum(nums)
    temp_sum = (len(nums)+1) * len(nums) / 2
    return int(temp_sum) - nums_sum


if __name__ == '__main__':
    res = missing_number([3, 0, 1])
    print(str(res))
