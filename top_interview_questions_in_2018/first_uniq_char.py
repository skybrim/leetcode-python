#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def first_uniq_char(s):
    store = []
    for i in range(len(s)):
        if s[i] not in s[i+1:]:
            if s[i] not in store:
                return i
        else:
            store.append(s[i])
    return -1
