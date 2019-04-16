
'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.


assumptions:
each element would be a single character
'''

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		length = len(board)
		for i in range(length):
			digits = list("".join(board[i]).replace('.', ''))
			if len(digits) > len(set(digits)):
				return False
			col = [row[i] for row in board]
			digits = list("".join(col).replace('.', ''))
			if len(digits) > len(set(digits)):
				return False
			tlcr = (i//3) * 3
			tlcc = i % 3 * 3
			sq = list()
			for j in range(tlcr, tlcr+3):
				for k in range(tlcc, tlcc+3):
					sq.append(board[j][k])
			digits = list("".join(sq).replace('.', ''))
			if len(digits) > len(set(digits)):
				return False
		return True