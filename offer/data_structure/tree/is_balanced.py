#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: is_balanced.py
@author: wiley
@datetime: 2020/7/3 10:29 AM

平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过 1，那么它就是一棵平衡二叉树。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root):
    """
    @param root: TreeNode
    @return: bool
    """
    def recur(node):
        if not node:
            return 0
        left = recur(node.left)
        if left == -1:
            return -1
        right = recur(node.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1

    return recur(root)


if __name__ == '__main__':
    pass
