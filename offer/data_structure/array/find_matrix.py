#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: find_matrix.py
@author: wiley
@datetime: 2020/5/12 10:38 AM

在二维数组中的查找
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增顺序排列。
请完成一个函数，输入这样的二维数组和一个整数，判断数组是否含有这个整数。
"""


def find(matrix, rows, columns, number):
    """
    :param matrix:  List[List[int]]
    :param rows: int
    :param columns: int
    :param number: int
    :return: bool
    """
    found = False
    if matrix and rows > 0 and columns > 0:
        cur_row = 0
        cur_column = columns - 1
        while cur_row < rows and cur_column >= 0:
            if matrix[cur_row][cur_column] == number:
                found = True
                break
            elif matrix[cur_row][cur_column] > number:
                cur_column -= 1
            else:
                cur_row += 1
        return found


if __name__ == '__main__':
    pass
