#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def intersect(nums1, nums2):
    result = []
    if len(nums1) < len(nums2):
        for num in nums1:
            if num in nums2:
                result.append(num)
    else:
        for num in nums2:
            if num in nums1:
                result.append(num)
    return result

