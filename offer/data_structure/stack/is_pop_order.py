#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: is_pop_order.py
@author: wiley
@datetime: 2020/6/3 9:25 AM

栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出序列。
假设压入栈的所有数字均不相等。
"""


def validate_stack_sequences(pushed, popped):
    help_stack = []
    index = 0
    for num in pushed:
        help_stack.append(num)
        while help_stack and help_stack[-1] == popped[index]:
            help_stack.pop()
            index += 1
    return not help_stack


if __name__ == '__main__':
    res = validate_stack_sequences([1, 2, 3, 4, 5], [5, 3, 4, 2, 1])
    print(res)
    pass
