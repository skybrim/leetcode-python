#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: sum_nums.py
@author: wiley
@datetime: 2020/7/16 9:26 AM

求 1+2+...+n
求1+2+...+n，要求不能使用乘除法、for、while、if、else、switch、case 等关键字及判断语句（A?B:C）.
"""

def sum_nums(n):
	return n and (sum_nums(n - 1) + n)
	
print(sum_nums(3))