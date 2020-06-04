#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: verify_sequence_of_bst.py
@author: wiley
@datetime: 2020/6/4 9:36 AM

二叉搜索树的后续遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
假设输入的数组的任意两个数字都不相同。
"""


def verify_sequence_of_bst(sequence):
    """
    @param sequence: List[int]
    @return: bool
    """
    def recur(i, j):
        if i >= j:
            return True
        p = i
        while sequence[p] < sequence[j]:
            p += 1
        m = p
        while sequence[p] > sequence[j]:
            p += 1
        return p == j and recur(i, m - 1) and recur(m, j)

    return recur(0, len(sequence) - 1)


if __name__ == '__main__':
    result = verify_sequence_of_bst([4, 6, 7, 5])
    print(result)
    pass
