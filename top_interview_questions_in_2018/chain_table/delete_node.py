#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: delete_node.py
@author: wiley
@datetime: 2020/4/30 10:52 AM

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Given linked list -- head = [4, 5, 1, 9], which looks like following:
4 -> 5 -> 1 -> 9
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    """
    :param node: ListNode
    :return: void Do not return anything.
    """
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    pass
