'''
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		sintervals = sorted(intervals)
		hasMerge = True
		
		while hasMerge:
			hasMerge = False
			i = 0
			while i < len(sintervals)-1:
				curr = sintervals[i]
				nxt = sintervals[i+1]
				if curr[1] >= nxt[0]:
					hasMerge = True
					sintervals[i][0] = min(curr[0], nxt[0])
					sintervals[i][1] = max(curr[1], nxt[1])
					sintervals.pop(i+1)
				else:
					i +=1
		return sintervals