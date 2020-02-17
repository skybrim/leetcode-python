#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)

rotate([1, 2, 3, 4, 5, 6, 7], 3)
