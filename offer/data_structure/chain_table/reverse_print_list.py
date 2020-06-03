#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: reverse_print_list.py
@author: wiley
@datetime: 2020/5/14 9:49 AM

从尾到头打印链表
输入一个链表的头结点，从尾到头反过来返回每个节点的值（用数组返回）
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_print_recursive(head):
    """
    递归
    :param head: ListNode
    :return: List[int]
    """
    return reverse_print_recursive(head.next) + [head.val] if head else []


def reverse_print_stack(head):
    """
    栈
    :param head: ListNode
    :return: List[int]
    """
    store = [head.val]
    while head.next:
        head = head.next
        store += [head.val]
    return store[::-1]


if __name__ == '__main__':
    pass
