#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 10:55 上午
# @Author  : Wiley
# @Email   : throughskybrim@gmail.com
# @File    : product_except_self.py


def product_except_self(nums):
    res = []
    k = 1
    for i in range(len(nums)):
        res.append(k)
        k = k * nums[i]
    k = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i] * k
        k = k * nums[i]
    return res


if __name__ == "__main__":
    res = product_except_self([1, 2, 3, 4])
    print(res)