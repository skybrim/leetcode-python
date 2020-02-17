#!/usr/bin/env python
# -*- coding: utf-8 -*-


def search_matrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    x, y = 0, m-1
    while True:
        if x > n-1:
            return False
        if y < 0:
            return False
        if matrix[y][x] < target:
            x += 1
        elif matrix[y][x] > target:
            y -= 1
        else:
            return True
    return False
