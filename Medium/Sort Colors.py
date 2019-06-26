'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		RED = 0
		WHITE = 1
		BLUE = 2
		r = 0
		b = 0
		i = 0
		last = len(nums)-1
		
		while i <= last - b:
			if nums[i] == RED:
				nums[r], nums[i] = nums[i], nums[r]
				r += 1
				i += 1
				continue
			if nums[i] == BLUE:
				nums[i], nums[last - b] = nums[last - b], nums[i]
				b += 1
				continue
			if nums[i] == WHITE:
				i +=1
			
		
	 
				