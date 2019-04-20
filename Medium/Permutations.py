'''
https://leetcode.com/problems/permutations/submissions/

Given a collection of distinct integers, return all possible permutations.
'''


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		results = list()
		self.c(nums.copy(), results, list())
		return results


	# trivial; use python lib
	def a(self, nums):
		return list(itertools.permutations(nums))




	def b(self, nums, results, per):
		if len(nums) == 0:
			results.append(per.copy())
			return

		next_nums = nums.copy()

		while len(nums) > 0:
			next_nums.pop()
			curr = nums.pop()

			per.append(curr)

			self.p(next_nums.copy(), results, per)
			next_nums.insert(0, per.pop())



    # very similar to solution b; more elegant :)
    def c(self, nums, results, per):
        if len(nums) == 0:
            results.append(per.copy())
            return
        
        for i in range(len(nums)):
            per.append(nums[i])

            next_nums = nums[0:i] + nums[i+1:]

            self.p(next_nums,results, per)
            per.pop()