#!/usr/bin/env python
# -*- coding: utf-8 -*-


def super_egg_drop(K, N):
    T = 1
    while helper(K, T) < N+1:
        T += 1
    return T


def helper(K, T):
    if K == 1:
        return T
    if T == 1:
        return 2
    return helper(K-1, T-1) + helper(K, T-1)
