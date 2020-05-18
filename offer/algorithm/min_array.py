#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: min_array.py
@author: wiley
@datetime: 2020/5/18 10:37 AM

旋转数组的最小数字。
把一个数组最开始的若干个元素搬到数组的末尾，我们诚挚为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如 数组 【3, 4, 5, 1, 2】为【1, 2, 3, 4, 5】的一个旋转，该数组的最小值为 1、
"""


def min_array(numbers):
    """
    @param numbers: List[int]
    @return: int
    """
    start = 0
    end = len(numbers) - 1
    while start < end:
        mid = (start + end) // 2
        if numbers[mid] < numbers[end]:
            end = mid
        elif numbers[mid] > numbers[end]:
            start = mid + 1
        else:
            end -= 1
    return numbers[start]


if __name__ == '__main__':
    result = min_array([3, 4, 5, 1, 2])
    print(str(result))
