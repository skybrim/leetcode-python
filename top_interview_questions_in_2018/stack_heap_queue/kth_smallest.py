#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 9:57 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : kth_smallest.py
"""kth_smallest"""

import heapq


def kth_smallest(matrix, k):
    """
    Given a n x n matrix where each of the rows and columns
    are sorted in ascending order,
    find the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order,
    not the kth distinct element.
    """
    max_heap = []
    row, col = len(matrix), len(matrix[0])
    for i in range(row):
        for j in range(col):
            heapq.heappush(max_heap, -matrix[i][j])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
    return -max_heap[0]


if __name__ == "__main__":
    MATRIX = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    K = 8
    print(kth_smallest(MATRIX, K))
