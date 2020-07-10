#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: left_rotate_string.py
@author: wiley
@datetime: 2020/7/10 9:57 AM

左旋转字符串
字符串的坐旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数，实现字符串左旋转操作的功能。
举例：输入字符串 "abcdefg" 和数字 2，该函数将返回左旋转两位得到的结果 "cdefgab"
"""


def reverse_left_words(s, n):
    """
    @param s: str
    @param n: int
    @return: str
    """
    return s[n:] + s[:n]


def reverse_left_words_ii(s, n):
    res = ""
    for i in range(n, len(s)):
        res += s[i]
    for i in range(0, n):
        res += s[i]
    return res


if __name__ == '__main__':
    result = reverse_left_words_ii("abcdeft", 2)
    print(result)
