'''
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
Note:
Your solution should be in logarithmic complexity.
'''


class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		if not nums or len(nums) == 0: return None
		negativeInfinity = -sys.maxsize-1
		nums.insert(0, negativeInfinity)
		nums.append(negativeInfinity)
		
		i = 1
		while i < len(nums)-1:
			before = nums[i-1]
			after = nums[i+1]
			if nums[i] > before and nums[i] > after:
				return i-1
			
			before = nums[-i-2] #-i-1-1
			after = nums[-i] #-i-1+1
			if nums[-i-1] > before and nums[-i-1] > after:
				return len(nums)-2-i # we added 2 items to length
			i += 1
		return None