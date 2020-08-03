#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: max_sliding_window.py
@author: wiley
@datetime: 2020/08/03 

滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
"""

import collections

def max_sliding_window(nums, k):
	"""
	@param nums: List[int]
	@param k: int
	@return: List[int]
	"""
	deque = collections.deque()
	if not nums or k == 0:
		return []
	for i in range(k):
		while deque and deque[-1] < nums[i]:
			deque.pop()
		deque.append(nums[i])
	res = [deque[0]]
	for i in range(k, len(nums)):
		if deque[0] == nums[i-k]:
			deque.popleft()
		while deque and deque[-1] < nums[i]:
			deque.pop()
		deque.append(nums[i])
		res += [deque[0]]
	return res
	

print(max_sliding_window([4, 3, 11], 3))
	