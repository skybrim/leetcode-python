#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: reverse_list.py
@author: wiley
@datetime: 2020/5/22 10:53 AM

反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    cur = head
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


if __name__ == '__main__':
    pass
