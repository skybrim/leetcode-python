#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: length_of_longest_substring.py
@author: wiley
@datetime: 2020/08/07

最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
"""

def lenght_of_longest_substring(s):
	"""
	:param s: str
	:return: int
	"""
	hash_map = {}
	res = 0
	start, end = 0, 0
	for i in range(len(s)):
		if s[end] in hash_map:
			start = max(start, hash_map[s[end]] + 1)
		hash_map[s[end]] = i
		res = max(res, end - start + 1)
		end += 1
	return res
	
print(lenght_of_longest_substring('pwwkew'))
	