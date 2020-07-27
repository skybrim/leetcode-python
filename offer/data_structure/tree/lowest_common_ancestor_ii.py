#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@file: lowest_common_ancestor_ii.py
@author: wiley
@datetime: 2020/7/27 10:00 AM

二叉树的最近公共祖先 II
给定一个二叉树，找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。
"""


def lowest_common_ancestor_ii(root, p, q):
	if not root or root == p or root == q:
		return root
	left = lowest_common_ancestor_ii(root.left, p, q)
	right = lowest_common_ancestor_ii(root.right, p, q)
	if not left:
		return right
	if not right:
		return left
	return root