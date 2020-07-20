#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: exist.py
@author: wiley
@datetime: 2020/7/20 10:38 AM

矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如：
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
包含一条字符串 “bfce” 的路径，但不含字符串“abfb”的路径
"""


def exist(board, word):
	"""
	@param board: List[List[str]]
	@param word: str
	@return: bool
	"""
	def dfs(row, column, cur):
		if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or word[cur] != board[row][column]:
			return False
		if cur == len(word) - 1:
			return True
		temp, board[row][column] = board[row][column], ''
		res = dfs(row + 1, column, cur + 1) or dfs(row - 1, column, cur + 1) or dfs(row, column + 1, cur + 1)  or dfs(row, column - 1, cur + 1)
		return res
	
	for row in range(len(board)):
		for column in range(len(board[0])):
			if dfs(row, column, 0):
				return True
	return False
			
			
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))