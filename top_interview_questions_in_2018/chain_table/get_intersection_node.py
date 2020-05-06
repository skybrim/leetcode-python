#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: get_intersection_node.py
@author: wiley
@datetime: 2020/5/6 9:50 AM

Write a program to find the node at which the intersection of two singly linked lists begins.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(head_a, head_b):
    """
    :param head_a: ListNode
    :param head_b: ListNode
    :return: ListNode
    """
    curr_a, curr_b = head_a, head_b
    while curr_a != curr_b:
        curr_a = curr_a.next if curr_a else head_b
        curr_b = curr_b.next if curr_b else head_a
    return curr_a


if __name__ == '__main__':
    pass
