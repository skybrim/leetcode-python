#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: tree_to_doubly_list.py
@author: wiley
@datetime: 2020/6/12 9:51 AM

二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树种节点指针的指向。
"""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def tree_to_doubly_list(self, root):
        if not root:
            return None
        self.recur(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

    def recur(self, node):
        if not node:
            return
        self.recur(node.left)
        if self.pre:
            self.pre.right = node
            node.left = self.pre
        else:
            self.head = node
        self.pre = node
        self.recur(node.right)


if __name__ == '__main__':
    pass
