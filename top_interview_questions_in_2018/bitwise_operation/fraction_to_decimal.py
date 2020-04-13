#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wiley
# datetime:2020/4/13 9:32 AM

"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.
if the fractional part is repeating, enclose the repeating part in parentheses.
"""


def fraction_to_decimal(numerator, denominator):
    """fraction_to_decimal"""
    if numerator == 0:
        return "0"
    result = []
    # 判断正负
    if (numerator > 0) ^ (denominator > 0):
        result.append("-")
    numerator, denominator = abs(numerator), abs(denominator)
    # 判断是否整除
    quotient, remainder = numerator // denominator, numerator % denominator
    result.append(str(quotient))
    # 余数 == 0，整除
    if remainder == 0:
        return "".join(result)
    # 余数 > 0, 非整数
    result.append(".")
    store = {remainder: len(result)}
    while remainder > 0:
        remainder *= 10
        quotient, remainder = remainder // denominator, remainder % denominator
        result.append(str(quotient))
        # 出现重复的余数，说明开始循环
        if remainder in store:
            result.insert(store[remainder], "(")
            result.append(")")
            break
        store[remainder] = len(result)
    return "".join(result)


if __name__ == '__main__':
    res = fraction_to_decimal(5, 1)
    print(str(res))
