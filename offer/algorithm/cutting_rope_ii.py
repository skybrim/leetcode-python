#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: cutting_rope_ii.py
@author: wiley
@datetime: 2020/07/22

剪绳子 II
给一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段。m、n 都是整数，且m>1和n>1，每段绳子长度记作 k[0],k[1]...k[m-1]。
请问，k[0]*k[1]*...*k[m-1]可能的最大乘积是多少。
答案需要取模 1e9+7

举例：绳子长度是 8，把绳子剪成长度为 2、3、3 的三段，此时得到的最大乘积是 18。
"""


def cutting_rope_ii(n):
	"""
	@param n: int
	@return: int
	"""
	if n <= 3:
		return n - 1
	a = n // 3 - 1 # 分成 a 段
	b = n % 3 # 根据结果确定最后一段如何处理
	p = 1000000007 # 除数
	x = 3 
	rem = 1
	while a > 0:
		if a % 2:
			rem = (rem * x) % p
		x = x ** 2 % p
		a //= 2
	if b == 0:
		return (rem * 3) % p
	if b == 1:
		return (rem * 4) %p
	# b == 2
	return (rem * 6) % p
	
cutting_rope_ii(3)