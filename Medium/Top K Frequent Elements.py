'''
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		# num = None
		# count = 0
		# results = [(num, count)] * k
		results = list()
		
		nums.sort()
		n, count = nums[0], 0
		for i in range(len(nums)):
			if nums[i] == n:
				count +=1
			else:
				results.append((count, n))
				n, count = nums[i], 1
		results.append((count, n))
		
		results.sort(reverse=True)
		return [tup[1] for tup in results[:k]]

				