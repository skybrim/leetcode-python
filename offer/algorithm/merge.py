#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: merge.py
@author: wiley
@datetime: 2020/5/25 10:26 AM

合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    """
    @param l1: ListNode
    @param l2: ListNode
    @return: ListNode
    """
    if not l1:
        return l2
    elif not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


if __name__ == '__main__':
    pass
