#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/7 10:20 AM

"""Reverse bits of a given 32 bits unsigned integer."""


def reverse_bits(n):
    """Reverse bits"""
    result, offset = 0, 31
    while n:
        result += (n & 1) << offset
        n = n >> 1
        offset -= 1
    return result


if __name__ == '__main__':
    res = reverse_bits(0b00000010100101000001111010011100)
    print(bin(res))
