'''
https://leetcode.com/problems/subsets/


Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = list()
        for sublen in range(len(nums)+1):
            sub = list()
            self.recurse(nums, 0, sublen, sub, results)

        return results


    def recurse(self, nums, startI, sublen, sub, results):
        if len(sub) == sublen:
            results.append(sub.copy())
            return

        while startI < len(nums):
            n = nums[startI]
            sub.append(n)
            self.recurse(nums, startI+1, sublen, sub, results)
            sub.pop()
            startI +=1