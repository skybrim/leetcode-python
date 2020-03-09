# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>


def find_words(board, words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = 1

    row, col = len(board), len(board[0])
    res = set()

    def dfs(i, j, node, pre, visited):
        if '#' in node:
            res.add(pre)
        for (di, dj) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            _i, _j = i + di, j + dj
            if -1 < _i < row\
                and -1 < _j < col\
                and board[_i][_j] in node\
                and (_i, _j) not in visited:
                dfs(_i, _j, node[board[_i][_j]], pre + board[_i][_j],
                    visited | {(_i, _j)})

    for i in range(row):
        for j in range(col):
            if board[i][j] in trie:
                dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})

    return list(res)


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(find_words(board, words))
