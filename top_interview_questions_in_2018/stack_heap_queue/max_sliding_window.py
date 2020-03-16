# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>
"""
Given an array nums, there is a sliding window of size
k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.
"""


def max_sliding_window(nums, k):
    """max_sliding_window"""
    if not nums:
        return []
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i + k]))
    return res
