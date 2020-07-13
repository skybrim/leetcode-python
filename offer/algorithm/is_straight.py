#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: is_straight.py
@author: wiley
@datetime: 2020/7/13 2:25 PM

扑克牌中的顺子
从扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这 5 张牌是不是连续的。
2~10 为数字本身，A 为 1，J 为 11，Q 为 12，K 为 13，大小王为 0，可以看成任意数字。A 不能视为 14。
"""


def is_straight(nums):
    """
    @param nums: List[int]
    @return: bool
    """
    is_repeat = set()
    min_num, max_num = 14, 0
    for num in nums:
        if num == 0:
            continue
        if num in is_repeat:
            return False
        is_repeat.add(num)
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    return max_num - min_num < 5


def is_straight_ii(nums):
    joker = 0
    nums.sort()
    for i in range(4):
        if nums[i] == 0:
            joker += 1
            continue
        if nums[i] == nums[i + 1]:
            return False
    return nums[4] - nums[joker] < 5


if __name__ == '__main__':
    result = is_straight([1, 2, 3, 4, 5])
    print(result)
