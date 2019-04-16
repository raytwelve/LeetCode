'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.




00  01  02  03  04
10  11  12  13  14
20  21  22  23  24
30  31  32  33  34
40  41  42  43  44

i=0,1,2
j=0,1,2,3
j=1,2
j=2

20 -> 00
22 -> 20
02 -> 22
00 -> 02

10 -> 01
21 -> 10
12 -> 21
01 -> 12

11 -> 11

'''


class Solution:
	def rotate(self, board: List[List[int]]) -> None:
		length = len(board)
		last = length-1
		for i in range((length+1)//2):
			for j in range(i, last-i):
				tmp = board[i][j]
				# blc -> tlc
				board[i][j] = board[last-j][i]
				# brc -> blc
				board[last-j][i] = board[last-i][last-j]
				# trc -> brc
				board[last-i][last-j] = board[j][last-i]
				# tlc -> trc
				board[j][last-i] = tmp