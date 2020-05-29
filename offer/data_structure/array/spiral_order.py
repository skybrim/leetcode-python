#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: spiral_order.py
@author: wiley
@datetime: 2020/5/29 10:05 AM

顺时针打印矩阵
输入一个矩阵，按照从外向里的顺序依次打印出每一个数字。
"""


def spiral_order(matrix):
    """
    @param matrix: List[List[int]]
    @return: List[int]
    """
    res = []
    if not matrix:
        return res
    top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
    while True:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        if top > bottom:
            break
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if right < left:
            break
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        if bottom < top:
            break
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        if left > right:
            break
    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    temp = spiral_order(matrix)
    print(temp)
