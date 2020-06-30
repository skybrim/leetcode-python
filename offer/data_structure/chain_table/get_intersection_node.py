#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: get_intersection_node.py
@author: wiley
@datetime: 2020/6/30 10:15 AM

两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(head_a, head_b):
    """
    @param head_a: ListNode
    @param head_b: ListNode
    @return: ListNode
    """
    if not head_a or not head_b:
        return None
    cur_a, cur_b = head_a, head_b
    while cur_a is not cur_b:
        cur_a = cur_a.next if cur_a else head_b
        cur_b = cur_b.next if cur_b else head_a
    return cur_a


if __name__ == '__main__':
    pass
