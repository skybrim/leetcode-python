#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/26 10:29 AM

"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. if pos is -1, then there is no cycle in the linked list.
"""


class ListNode(object):
    """ Definition for singly-linked list."""

    def __init__(self, x):
        """__init__"""
        self.val = x
        self.next = None


def has_cycle(head):
    """
    :type head: ListNode
    :rtype bool
    """
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


if __name__ == '__main__':
    pass
