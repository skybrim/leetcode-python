#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: MinStack.py
@author: wiley
@datetime: 2020/6/1 10:53 AM

包含 min 函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数
在该栈中，调用 min、push、pop 的时间复杂度都是 O(1)
"""


class MinStack(object):

    def __init__(self):
        """
        initialize
        """
        self.stack = []
        self.help_stack = []

    def push(self, x):
        """
        push
        @param x: int
        @return: None
        """
        self.stack.append(x)
        if not self.help_stack or self.help_stack[-1] >= x:
            self.help_stack.append(x)

    def pop(self):
        if self.help_stack[-1] == self.stack.pop():
            self.help_stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.help_stack[-1]


if __name__ == '__main__':
    pass
