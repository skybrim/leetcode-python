#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: single_numbers_ii.py
@author: wiley
@datetime: 2020/7/29 9:08 PM

数组中只出现一次的数字 II
在一个整数数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
请找出那个只出现一次的数字。
"""


def singleNumber(nums):
	"""
	@param nums: List[int]
	@return: int
	"""
	res = 0
	for i in range(32):
		cnt = 0
		bit = 1 << i
		for num in nums:
			if num & bit != 0:
				cnt += 1
		if cnt % 3 != 0:
			res = res | bit
		
	return res - 2 ** 32 if res > 2 ** 31 - 1 else res