#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: two_sum.py
@author: wiley
@datetime: 2020/7/6 9:13 AM

和为 s 的两个数字
输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使得它们的和刚好是 s。
如果有多对数字的和等于 s，则输出任意一对即可。
"""


def two_sum(nums, target):
    """
    @param nums: List[int]
    @param target: int
    @return: List[int]
    """
    if not nums or nums[0] > target:
        return []
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [nums[i], nums[j]]
    return []


if __name__ == '__main__':
    result = two_sum([2, 7, 11, 15], 9)
    print(result)
