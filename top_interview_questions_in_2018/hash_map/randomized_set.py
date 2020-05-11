#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: randomized_set.py
@author: wiley
@datetime: 2020/5/11 10:02 AM

Design a data structure that supports all following operations in average O(1) time.
1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. get_random: Returns a random element from current set of elements. Each element must have the same probability
of being returned.
"""
from random import choice


class RandomizedSet(object):

    def __init__(self):
        """
        Initialized your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        Insert a value to the set. Returns true if the set did not already contain the specified element.
        :param val: int
        :return: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :param val: int
        :return: bool
        """
        if val in self.dict:
            last_val = self.list[-1]
            val_index = self.dict[val]
            self.list[val_index] = last_val
            self.list.pop()
            self.dict[last_val] = val_index
            del self.dict[val]
            return True
        return False

    def get_random(self):
        """
        Get a random element from set.
        :return: int
        """
        return choice(self.list)
