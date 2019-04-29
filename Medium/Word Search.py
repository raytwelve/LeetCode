'''
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		r, c = len(board), len(board[0])
		if len(word) > r*c: return False

		for i in range(r):
			for j in range(c):
				ij = (i,j)
				if board[i][j] == word[0]:
					visited = list()
					visited.append(ij)
					if self.checkDirections(board, ij, word[1:], visited): return True
		return False

	def checkDirections(self, board, ij, word, visited):
		if len(word) < 1: return True
		i, j = ij[0], ij[1]
		letter = word[0]
		up = (i, j-1)
		down = (i, j+1)
		left = (i-1, j)
		right = (i+1, j)
	 
		if self.checkMatch(board, right, letter, visited):
			visited.append(right)
			if self.checkDirections(board, right, word[1:], visited): return True
			visited.pop()
		if self.checkMatch(board, down, letter, visited):
			visited.append(down)
			if self.checkDirections(board, down, word[1:], visited): return True
			visited.pop()
		if self.checkMatch(board, left, letter, visited):
			visited.append(left)
			if self.checkDirections(board, left, word[1:], visited): return True
			visited.pop()
		if self.checkMatch(board, up, letter, visited):
			visited.append(up)
			if self.checkDirections(board, up, word[1:], visited): return True
			visited.pop()
		return False

	def checkMatch(self, board, ij, letter, visited):
		i, j = ij[0], ij[1]
		r, c = len(board), len(board[0])
		return i > -1 and j > -1 and i < r and j < c and ij not in visited and board[i][j] == letter