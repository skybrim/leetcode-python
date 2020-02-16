#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 10:38 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : median_finder.py


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def add_num(self, num: int) -> None:
        self.array.append(num)

    def find_median(self) -> float:
        count = len(self.array)
        if count == 0:
            return 0
        self.array.sort()
        if (count & 1) == 0:
            return (self.array[count//2] + self.array[count//2-1])/2
        else:
            return self.array[count//2]
