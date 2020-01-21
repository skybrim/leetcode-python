#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string


def is_palindrome(s):
    s = s.replace(' ', '')
    s = s.lower()
    dict = str.maketrans('', '', string.punctuation)
    s = s.translate(dict)
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


message = is_palindrome('race a car')
print(message)
