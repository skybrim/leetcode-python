#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 11:14 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : min_stack.py


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.helper_stack) == 0:
            self.helper_stack.append(x)
        elif self.helper_stack[-1] >= x:
            self.helper_stack.append(x)

    def pop(self):
        pop = self.stack.pop()
        if pop == self.helper_stack[-1]:
            self.helper_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.helper_stack[-1]


