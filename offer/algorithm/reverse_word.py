#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: reverse_word.py
@author: wiley
@datetime: 2020/7/9 9:36 AM

反转单词顺序
输入一个英文句子，反转句子中单词的顺序，但单词内字符的顺序不变。
标点符号和普通字母一样处理。
举例： 输入"I am a student."，输出"student. a am I"
"""


def reverse_word(s):
    """
    @param s: str
    @return: str
    """
    res = s.split()
    res.reverse()
    return " ".join(res)


def reverse_word_pro(s):
    s = s.strip()
    i, j = len(s) - 1, len(s) - 1
    res = []
    while i >= 0:
        while i >= 0 and s[i] != " ":
            i -= 1
        res.append(s[i + 1:j])
        while s[i] == " ":
            i -= 1
        j = i
    return " ".join(res)


if __name__ == '__main__':
    pass
