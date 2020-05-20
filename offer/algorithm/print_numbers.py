#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: print_numbers.py
@author: wiley
@datetime: 2020/5/20 10:19 AM

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999
"""


def print_numbers(n):
    if n < 0:
        return
    numbers = ['0'] * n
    for i in range(10):
        numbers[0] = str(i)
        help_recursive(numbers, n, 0)


def help_recursive(numbers, length, index):
    if index == length - 1:
        help_print(numbers)
        return
    for i in range(10):
        numbers[index + 1] = str(i)
        help_recursive(numbers, length, index+1)


def help_print(numbers):
    index = 0
    for num in numbers:
        if num != '0':
            print("".join(numbers[index:]))
            break
        index += 1


if __name__ == '__main__':
    print_numbers(3)
