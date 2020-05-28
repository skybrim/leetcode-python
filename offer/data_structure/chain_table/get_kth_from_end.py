#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: get_kth_from_end.py
@author: wiley
@datetime: 2020/5/22 10:36 AM

输入一个链表，输出该链表中倒数第 k 个节点。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_kth_from_end(head, k):
    if not head or k == 0:
        return None
    fast = head
    slow = head
    index = 0
    while fast:
        fast = fast.next
        index += 1
        if index > k:
            slow = slow.next
    return slow



if __name__ == '__main__':
    pass
