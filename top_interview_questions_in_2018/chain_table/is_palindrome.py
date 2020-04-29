#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: is_palindrome.py
@author: wiley
@datetime: 2020/4/29 10:02 AM

Given a singly linked list, determine if it is a palindrome.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def is_palindrome(head):
    """
    :param head: ListNode
    :return: bool
    """
    pre = head
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        temp = pre
        pre = slow
        slow = slow.next
        pre.next = temp
    if fast:
        slow = slow.next
    while slow and pre:
        if slow.val != pre.val:
            return False
        slow = slow.next
        pre = pre.next
    return True


if __name__ == '__main__':
    pass
