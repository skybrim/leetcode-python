#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def increasing_triplet(nums):
    if len(nums) < 3:
        return False
    minNum = 2**32-1
    midNum = 2**32-1
    for num in nums:
        if num < minNum:
            minNum = num
        if num > minNum and num < midNum:
            midNum = num
        if num >midNum:
            return True
    return False
