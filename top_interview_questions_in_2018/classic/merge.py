#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge(nums1, m, nums2, n):
    point = 0
    for num in nums2:
        while num > nums1[point]:
            if point == m:
                break
            point += 1
        del nums1[-1]
        nums1.insert(point, num)
        m += 1
