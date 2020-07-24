#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: missing_number.py
@author: wiley
@datetime: 2020/07/23

0~n-1中缺失的数字
一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0~n-1 之内。
在范围 0~n-1 内的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""


def missing_number(nums):
	"""
	@param nums: List[int]
	@return: int
	"""
	n = len(nums) + 1
	total_sum = (0 + n-1) * n // 2
	cur_sum = 0
	for num in nums:
		cur_sum += num
	return total_sum - cur_sum
	
	
def missing_number_ii(nums):
	i, j = 0, len(nums) - 1
	while i <= j:
		m = (i + j) // 2
		if nums[m] == m:
			i = m + 1
		else:
			j = m - 1
	return i