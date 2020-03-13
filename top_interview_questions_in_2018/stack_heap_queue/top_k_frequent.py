# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>


def top_k_frequent(nums, k):
    temp = {}
    for num in nums:
        temp.setdefault(num, 0)
        temp[num] = temp[num] + 1
    sortRes = sorted(temp.items(), key=lambda item:item[1], reverse = True)
    res = []
    for little in sortRes:
        res.append(little[0])
        if res.count == k:
            break
    return res
    



