#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: dice_sum
@author: wiley
@datetime: 2020/7/12 9:06 PM

n个骰子的点数
把 n 个骰子仍在地上，所有骰子朝上一面的点数之和为 s。
输入 n，打印出 s 的所有可能的值出现的概率
"""


def dice_sum(n):
    """
    @param n: int
    @return: List[float]
    """
    dp = [0] * (6 * n + 1)
    for i in range(1, 7):
        dp[i] = 1
    for i in range(2, n + 1):
        for j in range(6 * i, i - 1, -1):
            dp[j] = 0
            for cur in range(1, 7):
                if j - cur < i - 1:
                    break
                dp[j] = dp[j] + dp[j - cur]
    total = 6 ** n
    res = []
    for i in range(n, 6 * n + 1):
        res.append(dp[i] * 1.0 / total)
    return res

