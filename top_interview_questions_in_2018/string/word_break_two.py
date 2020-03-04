# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>
"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.
"""

#  from typing import List
from collections import deque


def word_break(s, word_dict):
    size = len(s)

    # 非空字符串
    assert size > 0

    # 把 word_dict 放入哈希表
    word_set = {word for word in word_dict}

    # 创建 dp
    # dp[i] 表示长度为 i 的 s，满足题目
    # 0 表示 False， 1 表示 True
    dp = [0 for _ in range(size + 1)]
    dp[0] = 1

    for i in range(1, size + 1):
        # i 表示 string 子串的长度
        for j in range(i):
            # j 表示后子串的起始位置，最大 i-1
            # j 也表示前子串的长度
            # dp[j] 写前面会更快，否则还要切片，在放入hash 表判重
            if dp[j] and s[j:i] in word_set:
                dp[i] = 1
                break

    res = []
    # 如果有解，开始回溯
    if dp[-1]:
        queue = deque()
        dfs(s, size, word_set, res, queue, dp)
    return res


def dfs(s, length, word_set, res, path, dp):
    if length == 0:
        res.append(' '.join(path))
        return
    for i in range(length):
        if dp[i]:
            suffix = s[i:length]
            if suffix in word_set:
                path.appendleft(suffix)
                dfs(s, i, word_set, res, path, dp)
                path.popleft()


print(word_break('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']))
