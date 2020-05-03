#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: odd_even_list.py
@author: wiley
@datetime: 2020/5/3 5:28 PM

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def odd_even_list(head):
    """
    :param head: ListNode
    :return: ListNode
    """
    if not head:
        return None
    odd_head = head
    even_head = head.next
    even_temp = even_head
    while even_head and even_head.next:
        odd_head.next = even_head.next
        odd_head = odd_head.next
        even_head.next = odd_head.next
        even_head = even_head.next
    odd_head.next = even_temp
    return head


if __name__ == '__main__':
    pass
