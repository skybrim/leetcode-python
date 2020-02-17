#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(s):
    result = []

    def help(sub_s, temp):
        if not sub_s:
            result.append(temp)
        for i in range(1, len(sub_s)+1):
            if sub_s[:i] == sub_s[:i][::-1]:
                help(sub_s[i:], temp + [s[:i]])

    help(s, [])
    return result
