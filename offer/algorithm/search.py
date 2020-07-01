#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: search.py
@author: wiley
@datetime: 2020/7/1 9:36 AM

在排序数组中查找数字
统计一个数字在排序数组中出现的次数。
"""


def search(nums, target):
    """
    @param nums: List[int]
    @param target: int
    @return: int
    """
    if target not in nums:
        return 0

    def helper(tar):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] <= tar:
                i = mid + 1
            else:
                j = mid - 1
        return i

    return helper(target) - helper(target - 1)


if __name__ == '__main__':
    result = search([5, 7, 7, 8, 8, 10], 8)
    print(result)
