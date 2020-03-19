# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>
"""
Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer,
or a list -- whose elements may also be integers or other lists.
"""


class NestedIterator:
    """NestedIterator"""
    def __init__(self, nested_list):
        """init"""
        def build_generator(nested_list):
            for i in nested_list:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    i = i.getList()
                    for j in build_generator(i):
                        yield j

        self.g = build_generator(nested_list)

    def next(self):
        """
        return next
        """
        return self.v

    def has_next(self):
        """
        return true if nested_list flatten over
        """
        try:
            self.v = next(self.g)
            return True
        except:
            return False
