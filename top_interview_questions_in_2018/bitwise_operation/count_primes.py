#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/15 9:45 AM

"""
Count the number of prime numbers less than a non-negative number, n.
"""


def count_primes(n):
    """
    :type n: int
    :rtype int
    """
    # 创建全是 true 的数组，记录当前 index 的数字是否是素数
    store = [1] * n
    # 统计有多少个素数
    count = 0
    # 遍历
    for i in range(2, n):
        # 如果当前数字是素数，那么它的倍数都不是素数
        if store[i] == 1:
            count += 1
            for j in range(i*i, n, i):
                store[j] = 0
    return count


if __name__ == '__main__':
    res = count_primes(10)
    print(str(res))
