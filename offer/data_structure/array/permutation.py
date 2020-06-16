#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: permutation.py
@author: wiley
@datetime: 2020/6/16 9:21 AM

字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列
可以按任意顺序返回，但不能有重复元素。
"""


def permutation(s):
    """
    @param s: str
    @return: List[str]
    """
    res = []
    c = list(s)

    def dfs(x):
        if x == len(c) - 1:
            res.append(''.join(c))
            return
        temp = set()
        for i in range(x, len(c)):
            if c[i] in temp:
                continue
            temp.add(c[i])
            c[i], c[x] = c[x], c[i]
            dfs(x + 1)
            c[i], c[x] = c[x], c[i]

    dfs(0)
    return res


if __name__ == '__main__':
    temp = permutation('abc')
    print(temp)
