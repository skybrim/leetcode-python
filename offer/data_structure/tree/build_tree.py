#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: build_tree.py
@author: wiley
@datetime: 2020/5/15 1:54 PM

重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(pre_order, in_order):
    """
    :param pre_order: List[int]
    :param in_order: List[int]
    :return: TreeNode
    """
    if not pre_order:
        return None
    root = TreeNode(pre_order[0])
    index = in_order.index(pre_order[0])
    left_in_order = in_order[0:index]
    right_in_order = in_order[index+1:]
    left_pre_order = pre_order[1:1+len(left_in_order)]
    right_pre_order = pre_order[1+len(left_in_order):]
    left = build_tree(left_pre_order, left_in_order)
    right = build_tree(right_pre_order, right_in_order)
    root.left = left
    root.right = right
    return root


if __name__ == '__main__':
    pass
