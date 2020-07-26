#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@file: lowest_common_ancestor.py
@author: wiley
@datetime: 2020/7/26 10:00 AM

二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。
"""


class TreeNode:
	def def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
		
def lowest_common_ancestor(root, p, q):
	"""
	@param root: TreeNode
	@param p: TreeNode
	@param q: TreeNode
	@return: TreeNode
	"""
	if not root:
		return None
	while root:
		if p.val > root.val and q.val > root.val:
			root = root.right
		if p.val < root.val and q.val < root.val:
			root = root.left
		else:
			return root
	return None
	
	