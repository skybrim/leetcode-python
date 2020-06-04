#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: find_path.py
@author: wiley
@datetime: 2020/6/4 10:40 AM

二叉树中和为某一值得路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从根节点开始往下一值到叶节点所经过的节点形成一条路径
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_sum(root, expected_sum):
    """
    @param root: TreeNode
    @param expected_sum: int
    @return: List[List[int]]
    """
    result, path = [], []

    def recur(node, tar):
        if not node:
            return
        path.append(node.val)
        tar = tar - node.val
        if tar == 0 and not node.left and not node.right:
            result.append(path[:])
        recur(node.left, tar)
        recur(node.right, tar)
        path.pop()

    recur(root, expected_sum)
    return result


if __name__ == '__main__':
    pass
