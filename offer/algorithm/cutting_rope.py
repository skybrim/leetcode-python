#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: cutting_rope.py
@author: wiley
@datetime: 2020/7/21

剪绳子 I
给一个跟长度为 n 的绳子，请吧绳子剪成整数长度的 m 段（m、n 都是整数，n>1且m>1）。每段绳子的长度记为 k[0],k[1],...,k[m-1]。
问，k[0]*k[1]*...*k[m-1]可能的最大乘积是多少？
举例：绳子长度是 8，把绳子剪成长度为 2、3、3 的三段，此时得到的最大乘积是 18。
"""


def cutting_rope(n):
	"""
	@param n: int 
	@return: int 
	"""
	if n <= 3:
		return n - 1
	a, b = n // 3, n % 3
	if b == 0:
		return int(math.pow(3, a))
	if b == 1:
		return int(math.pow(3, a - 1) * 4)
	# b == 2
	return int(math.pow(3, a) * 2)