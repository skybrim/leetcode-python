#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/3 10:34 AM


"""Given an integer n, return the number of trailing zeroes in n!."""


def trailing_zeroes(n):
    result = 0
    while n >= 5:
        result += n // 5
        n = n // 5
    return result


if __name__ == '__main__':
    temp = trailing_zeroes(5)
    print(temp)
