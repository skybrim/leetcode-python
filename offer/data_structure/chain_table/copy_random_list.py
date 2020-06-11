#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: copy_random_list.py
@author: wiley
@datetime: 2020/6/11 9:22 AM

复杂链表的复制
请实现 copy_random_list 函数，复制一个复杂的链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = Node


def copy_random_list(head):
    """
    @param head: Node
    @return: Node
    """
    if not head:
        return None

    cur = head
    while cur:
        copy_node = Node(cur.val)
        copy_node.next = cur.next
        cur.next = copy_node
        cur = cur.next.next

    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    origin_list = head
    new_list = head.next
    copy_head = head.next
    while origin_list:
        origin_list.next = origin_list.next.next
        new_list.next = new_list.next.next if new_list.next else None
        origin_list = origin_list.next
        new_list = new_list.next

    return copy_head


if __name__ == '__main__':
    pass
