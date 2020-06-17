#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: majority_element.py
@author: wiley
@datetime: 2020/6/17 9:25 AM

数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
"""


def majority_element(nums):
    """
    @param nums: List[int]
    @return: int
    """
    result = nums[0]
    count = 1
    for num in nums[1:]:
        if count == 0:
            result = num
            count = 1
            continue
        if result == num:
            count += 1
        else:
            count -= 1
    return result


if __name__ == '__main__':
    temp = majority_element([10, 9, 9, 9, 10])
    print(temp)
    pass
