#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: CQueue.py
@author: wiley
@datetime: 2020/5/18 10:02 AM

用两个栈实现一个队列。
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )
"""


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, value):
        self.stack1.append(value)

    def delete_head(self):
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            temp = self.stack1.pop()
            self.stack2.append(temp)
        return self.stack2.pop()


if __name__ == '__main__':
    pass
