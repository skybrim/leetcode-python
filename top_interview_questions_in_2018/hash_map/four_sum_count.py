#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: four_sum_count.py
@author: wiley
@datetime: 2020/5/9 9:25 AM

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
All integers are in the range of -2**28 to 2**28 -1 and the result is guaranteed to be at mot 2**31 -1.
"""


def four_sum_count(A, B, C, D):
    """
    :param A: List[int]
    :param B: List[int]
    :param C: List[int]
    :param D: List[int]
    :return: int
    """
    res = 0
    sum_dict = {}
    for i in A:
        for j in B:
            sum_a_b = i + j
            if sum_a_b in sum_dict.keys():
                sum_dict[sum_a_b] = sum_dict[sum_a_b] + 1
            else:
                sum_dict[sum_a_b] = 1

    for k in C:
        for l in D:
            sum_c_d = -(k + l)
            if sum_dict[sum_c_d]:
                res += sum_dict[sum_c_d]

    return res


if __name__ == '__main__':
    pass
