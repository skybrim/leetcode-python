#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: find_continuous_sequence.py
@author: wiley
@datetime: 2020/7/7 9:39 AM

和为 s 的连续正数序列
输入一个正整数 target，输出所有和为 target 的连续正整数序列（至少含有两个数）。
系列内的数字由小到大排列，不同序列按照收个数字从小到大排列。
"""


def find_continuous_sequence(target):
    """
    @param target: int
    @return: List[List[int]]
    """
    result = []
    left, right = 1, 2
    while left < (1 + target) // 2:
        cur_sum = (left + right) * (right - left + 1) / 2
        if cur_sum < target:
            right += 1
        elif cur_sum > target:
            left += 1
        else:
            result.append(list(range(left, right + 1)))
            right += 1
    return result


if __name__ == '__main__':
    temp = find_continuous_sequence(9)
    print(temp)
