'''
https://leetcode.com/problems/permutations/submissions/

Given a collection of distinct integers, return all possible permutations.
'''


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		# trivial solution: python library function
		# return list(itertools.permutations(nums))


		results = list()
		self.p(nums.copy(), results, list())
		return results


	def p(self, nums, results, per):
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