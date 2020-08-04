#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: kth_largest.py
@author: wiley
@datetime: 2020/08/04

二叉搜索树的第 k 大节点
给定一棵二叉搜索树，找出其中第 k 大的节点。
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

def kth_largest(root, k):
	"""
	:param root: TreeNode
	:param k: int
	:return: int
	"""
	res = []
	
	def help_traversal(node):
		if not node or len(res) == k:
			return
		help_traversal(node.right)
		if len(res) == k:
			return
		res.append(node.val)
		if len(res) == k:
			return
		help_traversal(node.left)
	
	help_traversal(root)
	return res[-1]
	