#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: level_order.py
@author: wiley
@datetime: 2020/6/3 9:59 AM

从上向下打印二叉树
"""
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root):
    """
    从上到下打印出二叉树的每个节点，同一层节点按照从左到右的顺序打印
    @param root: TreeNode
    @return: List[int]
    """
    if not root:
        return []
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def level_order_ii(root):
    """
    从上到下打印二叉树，每一层的节点按从左到右的顺序打印，每一层打印一行
    @param root: TreeNode
    @return: List[List[int]]
    """
    if not root:
        return []
    queue = deque()
    result = []
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp)
    return result


def level_order_iii(root):
    """
    请实现一个函数，按照之字型打印二叉树
    @param root: TreeNode
    @return: List[List[int]]
    """
    if not root:
        return []
    queue = deque()
    queue.append(root)
    result = []
    index = 1
    while queue:
        temp = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if len(result) & 1:
                temp.appendleft(node.val)
            else:
                temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(temp))
    return result


if __name__ == '__main__':
    pass
