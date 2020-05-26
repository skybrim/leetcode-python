#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: heap_sort.py
@author: wiley
@datetime: 2020/5/26 11:40 AM

堆排序
给定一个整数数组，升序排列。
"""


def down_adjust(nums, parent_index, length):
    """
    下沉
    @param nums: 待调整的堆
    @param parent_index: 需要下沉的父节点
    @param length: 堆的有效大小
    @return: None
    """
    temp = nums[parent_index]
    child_index_left = parent_index * 2 + 1
    while child_index_left < length:
        # 存在右子节点且小于左子节点，前进至右节点
        if child_index_left + 1 < length and nums[child_index_left + 1] > nums[child_index_left]:
            child_index_left += 1
        # 小于所有子节点，跳出
        if temp >= nums[child_index_left]:
            break
        # 交换
        nums[parent_index] = nums[child_index_left]
        parent_index = child_index_left
        child_index_left = child_index_left * 2 + 1
    nums[parent_index] = temp


def heap_sort(nums):
    """
    堆排序
    @param nums: List[int]
    @return: List[int]
    """
    for i in range((len(nums) - 2) // 2, -1, -1):
        down_adjust(nums, i, len(nums))
    print(nums)
    for j in range(len(nums) - 1, -1, -1):
        nums[j], nums[0] = nums[0], nums[j]
        down_adjust(nums, 0, j)
    return nums


if __name__ == '__main__':
    result = heap_sort([5, 4, 3, 2, 1])
    print(result)
