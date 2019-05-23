'''
https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zRows = set()
        zCols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zRows.add(i)
                    zCols.add(j)

        for r in zRows:
            for i in range(len(matrix[r])):
                matrix[r][i] = 0
                
        for c in zCols:
            for i in range(len(matrix)):
                matrix[i][c] = 0