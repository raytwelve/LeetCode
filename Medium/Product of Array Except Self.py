'''
https://leetcode.com/problems/product-of-array-except-self/submissions/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


# Follow Up
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		space complexity would be:
			# O(c*n) = O(n),
			# for :
			# 	some constant c, where c = space used for one function call
			# 	and n = maxDepth of recursive calls aka size of input array
		results = [None] * len(nums)
		i = 0
		prod = 1
		hitEnd = False
		self.recurse(i, nums, results, prod, hitEnd)
		
		return results
		
					
	def recurse(self, i, nums, results, prod, hitEnd):
		if i == len(nums): return (True, 1)
		
		aprod = prod*nums[i]
		bprod = prod

		hitEnd, x = self.recurse(i+1, nums, results, aprod, hitEnd)
		aprod = x * nums[i]
		results[i] = x * bprod
		return hitEnd, x*nums[i]
		


# original solution; I DIVIDED :(
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		prod = 1
		prodExZero = 1
		zCount = 0
		results = list()
		
		for x in nums:
			prod *= x
			if x == 0: zCount += 1
			else: prodExZero *= x
				
		if zCount > 1: prodExZero = 0
				
		for i in range(len(nums)):
			if nums[i] == 0: results.append(prodExZero)
			else: results.append(int(prod/nums[i]))
		return results








