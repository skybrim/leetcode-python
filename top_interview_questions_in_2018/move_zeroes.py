#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def move_zeroes(nums):
    '''
    Do not return anything, modify nums in-place instead.
    '''
    zero_point = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            if zero_point > i or zero_point == -1:
                zero_point = i
            if nums[i] != 0 and zero_point != -1:
                nums[zero_point] = nums[i]
                nums[i] = 0
                zero_point += 1
