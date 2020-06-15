#!/usr/bin/env python
# -*- coding: utf-8 -*-


def super_egg_drop(K, N):
    T = 1
    while helper(K, T) < N+1:
        T += 1
    return T


def helper(K, T):
    if K == 1:
        return T
    if T == 1:
        return 2
    return helper(K-1, T-1) + helper(K, T-1)


def superEggDrop(self, K: int, N: int) -> int:
    """
    @param K: int
    @return: int
    """
    store = {}

    def dp(k, n):
        if (k, n) not in store:
            if n == 0:
                # 0 层楼
                result = 0
            elif k == 1:
                # 1 个鸡蛋，需要扔 n 次
                result = n
            else:
                # X 遍历
                low, high = 1, n
                # 二分搜索
                while low + 1 < high:
                    x = (low + high) // 2
                    t1 = dp(k - 1, x - 1)
                    t2 = dp(k, n - x)
                    if t1 < t2:
                        low = x
                    elif t1 > t2:
                        high = x
                    else:
                        low = high = x
                result = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (low, high))
            # 记录已经算过的值
            store[k, n] = result
        return store[k, n]

    return dp(K, N)
