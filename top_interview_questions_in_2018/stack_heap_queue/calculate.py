# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>
"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers,
+, -, *,/ operators and empty spaces .
The integer division should truncate toward zero.
"""
from collections import deque
import math

def calculate(s):
    """calculate"""
    def helper(s):
        """helper calculate"""
        stack = []
        sign = '+'
        num = 0

        while len(s) > 0:
            char = s.popleft()

            if char == '(':
                num = helper(s)
            if char == ')':
                break

            if char.isdigit():
                num = int(char) + 10 * num

            if (not char.isdigit() and char != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    temp = stack.pop()
                    res = temp * num
                    stack.append(res)
                elif sign == '/':
                    temp = stack.pop()
                    res = 0
                    if temp > 0:
                        res = temp // num
                    else:
                        res = math.ceil(temp / num)
                    stack.append(res)
                num = 0
                sign = char

        return sum(stack)

    return helper(deque(list(s)))
