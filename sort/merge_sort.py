#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: merge_sort.py
@author: wiley
@datetime: 2020/5/27 9:56 AM

排序数组
归并排序
"""


def merge_sort(nums):
    """
    归并排序
    @param nums: List[int]
    @return: List[int]
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])
    return merge(left_nums, right_nums)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


if __name__ == '__main__':
    result = merge_sort([5, 4, 3, 2, 1])
    print(result)
