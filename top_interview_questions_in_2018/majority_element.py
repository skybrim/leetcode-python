#!/usr/bin/env python
# -*- coding: utf-8 -*-


def majority_element(nums):
    res, count = nums[0], 1
    for num in nums[1:]:
        if count == 0:
            res = num
            count = 1
            continue
        if num == res:
            count += 1
        else:
            count -= 1
    return res
