#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: has_subtree.py
@author: wiley
@datetime: 2020/5/25 10:40 AM

树的子结构
输入两个二叉树 A 和 B，判断 B 是不是 A 的子结构。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_sub_structure(a, b):
    """
    @param a: TreeNode
    @param b: TreeNode
    @return: bool
    """

    def help_func(r1, r2):
        if not r2:
            return True
        if not r1:
            return False
        if r1.val != r2.val:
            return False
        return help_func(r1.left, r2.left) and help_func(r1.right, r2.right)

    result = False

    if not a or not b:
        return result

    if a.val == b.val:
        result = help_func(a, b)

    if not result:
        result = is_sub_structure(a.left, b)

    if not result:
        result = is_sub_structure(a.right, b)

    return result


if __name__ == '__main__':
    pass
