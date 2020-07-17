#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: find_repeat_number.py
@author: wiley
@datetime: 2020/7/17 9:26 AM

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0~n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
"""


def find_repeat_number(nums):
	"""
	@param nums: List[int]
	@return: int 
	"""
	temp_set = set()
	for num in nums:
		if num in temp_set:
			return num
		else:
			temp_set.add(num)
	return -1
	
print(find_repeat_number([2, 3, 1, 0, 2, 5, 3]))