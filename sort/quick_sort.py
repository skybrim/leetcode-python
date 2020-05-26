#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: quick_sort.py
@author: wiley
@datetime: 2020/5/26 9:58 AM

排序数组
给一个整数数组，升序排列
"""


def sort_array_quick(nums):
    """
    快排 递归 双边循环
    @param nums: List[int]
    @return: List[int]
    """
    def quick_sort(start, end):
        if start >= end:
            return
        pivot = nums[start]
        left, right = start, end
        while left != right:
            while left < right and nums[right] > pivot:
                right -= 1
            while left < right and nums[left] <= pivot:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[left] = nums[left], nums[start]
        quick_sort(start, left - 1)
        quick_sort(left + 1, end)
    quick_sort(0, len(nums) - 1)
    return nums


def sort_array_quick_single(nums):
    """
    快排 递归 单边循环
    @param nums: List[int]
    @return: List[int]
    """
    def quick_sort(start, end):
        if start >= end:
            return
        pivot = nums[start]
        index = start
        for k in range(start + 1, end + 1):
            if nums[k] < pivot:
                index += 1
                nums[index], nums[k] = nums[k], nums[index]
        nums[start], nums[index] = nums[index], nums[start]
        quick_sort(start, index - 1)
        quick_sort(index + 1, end)
    quick_sort(0, len(nums) - 1)
    return nums


if __name__ == '__main__':
    quick = sort_array_quick([5, 4, 3, 2, 1])
    print(quick)
