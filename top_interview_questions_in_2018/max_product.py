#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def max_product(nums):
    res, tmax, tmin = -sys.maxsize - 1, 1, 1
    for num in nums:
        if num < 0:
            tmax, tmin = tmin, tmax
        tmax = max(tmax * num, num)
        tmin = min(tmin * num, num)
        res = max(res, tmax)
    return res


res = max_product([-2, 0, -1])
print(res)
