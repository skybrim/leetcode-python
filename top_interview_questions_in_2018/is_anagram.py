#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_anagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False

res = is_anagram('rac', 'car')
print(res)
