##!/usr/bin/env python3
# -*- coding: utf-8 -*-


def first_unique_char(s):
    store = []
    for i in range(len(s)):
        if s[i] not in s[i+1:]:
            if s[i] not in store:
                return i
        else:
            store.append(s[i])
    return -1


if __name__ == '__main__':
    print(first_unique_char('abcda'))
