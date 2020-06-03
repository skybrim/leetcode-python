#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: delete_node.py
@author: wiley
@datetime: 2020/5/21 9:56 AM

在 O(1) 的时间删除链表节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(head, val):
    """
    val 为 int，时间复杂度 O(N)
    @param head: ListNode
    @param val: int
    @return: ListNode
    """
    if not head:
        return None
    if head.val == val:
        return head.next
    point = head
    while point.next and point.next.val != val:
        point = point.next
    point.next = point.next.next
    return head


def delete_node_s(head, val):
    """
    val 为 ListNode，时间复杂度为 O(1)，(O(1)×(n−1)+O(n))/n=O(1)
    信息交换
    @param head: ListNode
    @param val: ListNode
    @return: ListNode
    """
    if head == val:
        head = head.next
    elif val.next:
        val.val = val.next.val
        val.next = val.next.next
    else:
        point = head
        while point.next != val:
            point = point.next
        point.next = None
    return head


if __name__ == '__main__':
    pass
