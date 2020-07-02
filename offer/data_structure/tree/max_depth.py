#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: max_depth.py
@author: wiley
@datetime: 2020/7/2 10:31 AM

二叉树的深度
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root):
    """
    @param root: TreeNode
    @return: int
    """
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return left_depth + 1 if left_depth > right_depth else right_depth + 1


if __name__ == '__main__':
    pass
