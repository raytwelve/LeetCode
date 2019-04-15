'''
https://leetcode.com/problems/subsets/


Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''


class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		results = list()
		for sublen in range(len(nums)+1):
			self.recurse(nums, sublen, results)
		return results

	def recurse(self, nums, sublen, results, index=0, sub=list()):
		if len(sub) == sublen:
			results.append(sub.copy())
			return

		remainingSpots = sublen - len(sub)

		while index + remainingSpots <= len(nums):
			sub.append(nums[index])
			index +=1
			self.recurse(nums, sublen, results, index, sub)
			sub.pop()