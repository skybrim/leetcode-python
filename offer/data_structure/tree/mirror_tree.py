#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: mirror_tree.py
@author: wiley
@datetime: 2020/5/28 9:45 AM

二叉树的镜像
完成一个函数，输入一个二叉树，该函数输出它的镜像
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirror_tree(root):
    """
    镜像二叉树
    @param root: TreeNode
    @return: TreeNode
    """
    if not root:
        return None
    root.left, root.right = root.right, root.left
    root.left = mirror_tree(root.left)
    root.right = mirror_tree(root.right)
    return root


if __name__ == '__main__':
    pass
