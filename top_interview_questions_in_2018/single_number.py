#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def singleNumber(nums):
    res = nums[0]
    for num in nums[1:]:
        res ^= num
    return res

