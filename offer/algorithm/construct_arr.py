#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: construct_arr.py
@author: wiley
@datetime: 2020/07/28

构建乘积数组
给定一个数组 A[0, 1,..., n-1]，请构建一个数组 B[0, 1,..., n-1]。
其中 B 中的元素 B[i] = A[0] * A[1] *...* A[i-1] * A[i+1] *...* A[n-1]。
不能使用除法。
"""


def construct_arr(a):
	"""
	@param a: List[int]
	@return: List[int]
	"""
	left = [1] * len(a)
	right = [1] * len(a)
	for idx in range(1, len(a)):
		left[idx] = a[idx - 1] * left[idx - 1]
	for idx in range(len(a)-2, -1, -1):
		right[idx] = a[idx + 1] * right[idx + 1]
	for idx in range(len(a)):
		right[idx] = right[idx] * left[idx]
	return right
	
	
print(construct_arr([1,2,3,4,5]))


# left [1, 1, 2, 6, 24]
# right [120, 60, 20, 5, 1]