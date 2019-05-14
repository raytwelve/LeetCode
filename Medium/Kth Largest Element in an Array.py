'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		if not nums or k > len(nums): return None
		return sorted(nums)[-k]
		