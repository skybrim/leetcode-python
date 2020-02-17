#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def word_break(s, wordDict):
    store = {}

    def helper(point):
        if point == len(s):
            return True
        if point in store:
            return store[point]
        for i in range(point+1, len(s)+1):
            if s[point:i] in wordDict:
                if helper(i):
                    store[point] = True
                    return True
        store[point] = False
        return False

    return helper(0)
