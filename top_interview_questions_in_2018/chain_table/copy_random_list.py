#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/21 9:38 AM

"""
Definition for a Node.
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.copy_list = {}

    def copy_random_list(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        if head in self.copy_list:
            return self.copy_list[head]
        node = Node(head.val)
        self.copy_list[head] = node
        node.next = self.copy_random_list(head.next)
        node.random = self.copy_random_list(head.random)
        return node


if __name__ == '__main__':
    pass
