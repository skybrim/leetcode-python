#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        '''
        Resets the array to its original configuration and return it
        '''
        return self.nums

    def shuffle(self):
        temp_nums = self.nums[:]
        random.shuffle(temp_nums)
        return temp_nums
