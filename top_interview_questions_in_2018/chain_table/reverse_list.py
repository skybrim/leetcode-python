#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: reverse_list.py
@author: wiley
@datetime: 2020/4/28 11:06 AM

Reverse a singly linked list.
"""


class ListNode(object):
    """Definition for singly-linked list."""
    def __init__(self, x):
        """
        :param x: int
        """
        self.val = x
        self.next = None


def reverse_list(head):
    """
    :param head: ListNode
    :return: ListNode
    """
    if not head:
        return None

    def reverse(pre, next_node):
        """
        :param pre: ListNode
        :param next_node:  ListNode
        :return: ListNode
        """
        if not next_node:
            return pre
        temp = next_node.next
        next_node.next = pre
        return reverse(next_node, temp)

    head_next = head.next
    head.next = None
    return reverse(head, head_next)


if __name__ == '__main__':
    pass
