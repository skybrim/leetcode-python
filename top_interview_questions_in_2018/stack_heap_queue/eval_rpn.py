#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/20 9:43 AM

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +,-,*,/.
Each operand may be an integer or another expression.
Note:
    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there
    won't be any divide by zero operation.
"""


def eval_rpn(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            a, b = stack.pop(), stack.pop()
            stack.append(str(int(eval(b + token + a))))
        else:
            stack.append(token)
    return int(stack.pop())


if __name__ == '__main__':
    res = eval_rpn(['2', '1', '+', '3', '*'])
    print(res)
