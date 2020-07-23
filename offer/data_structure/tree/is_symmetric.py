#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: is_symmetric.py
@author: wiley
@datetime: 2020/07/23

对称的二叉树
请实现一个函数，判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
"""


 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def is_symmetric(root):
	"""
	@param root: TreeNode
	@return: bool
	"""
	def recursive_help(left, right):
		if not left and not right:
			return True
		if not left or not right or left.val != right.val:
			return False
		return recursive_help(left.right, right.left) and recursive_help(left.left, right.right)
		
	return recursive_help(root.left, root.right) if root else True