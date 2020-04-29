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
    if not head.next:
        return head
    pre = head
    cur = head.next
    pre.next = None
    while cur and cur.next:
        temp = pre
        pre = cur
        pre.next = temp
        cur = cur.next
    cur.next = pre
    return cur


if __name__ == '__main__':
    pass
