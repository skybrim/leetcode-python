#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 10:22 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : contain_duplicate.py


from collections import Counter


def contains_duplicate(nums):
    return len(nums) > len(set(nums))


if __name__ == "__main__":
    res = contains_duplicate([1, 1, 1, 3, 3, 4])
    print(res)
