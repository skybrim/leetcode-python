#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 11:09 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : find_Kth_largest.py


def find_kth_largest(nums, k):
    nums.sort()
    return nums[-k]
