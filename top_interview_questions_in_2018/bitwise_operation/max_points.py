#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/8 4:39 PM

"""
Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.
"""


def max_points(points):
    """find max points line."""
    if len(points) < 3:
        return len(points)
    result = 0
    for x in range(0, len(points)-1):
        temp_dict = {}
        repeat = 0
        for y in range(x + 1, len(points)):
            numerate = points[x][0] - points[y][0]
            denominator = points[x][1] - points[y][1]
            if denominator == 0 and numerate == 0:
                temp_dict.setdefault('0.0/0.0', 0)
                repeat += 1
                continue
            else:
                temp_gcd = gcd(numerate, denominator)
                numerate = numerate / temp_gcd
                denominator = denominator / temp_gcd
                slope = str(numerate) + '/' + str(denominator)
                if denominator == 0:
                    slope = '/0.0'
                if numerate == 0:
                    slope = '0.0/'
                temp_count = temp_dict.get(slope, 0)
                temp_count += 1
                temp_dict[slope] = temp_count
        result = max(result, max(list(temp_dict.values()))+1+repeat)
    return result


def gcd(a, b):
    while b != 0:
        temp = a % b
        a, b = b, temp
    return a


if __name__ == '__main__':
    res = max_points([[1,1],[2,2],[3,3]])
    print(res)
