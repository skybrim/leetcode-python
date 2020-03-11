#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 10:38 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : median_finder.py
"""
MedianFinder
"""
import heapq


class MedianFinder:
    """
    MedianFinder
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def add_num(self, num):
        """
        add num
        """
        self.count += 1
        heapq.heappush(self.max_heap, -num)
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def find_median(self):
        """
        find media
        """
        if self.count & 1:
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == "__main__":
    OBJ = MedianFinder()
    OBJ.add_num(1)
    OBJ.add_num(2)
    print(OBJ.find_median())
    OBJ.add_num(3)
    print(OBJ.find_median())
