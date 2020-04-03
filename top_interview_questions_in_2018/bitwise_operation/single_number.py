#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/2 3:13 PM

"""Given a non-empty array of integers, every element appears twice except for one. Find that single one."""


def single_number(nums):
    """find single number"""
    result = nums[0]
    for num in nums[1:]:
        result = result ^ num
    return result


if __name__ == '__main__':
    res = single_number([4, 1, 2, 1, 2])
    print(res)
