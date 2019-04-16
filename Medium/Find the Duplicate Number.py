'''
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.checkSet(nums)




        
    def checkSet(self, nums):
        visited = set()
        for x in nums:
            if x not in visited:
                visited.add(x)
            else:
                return x

    def pythonic(self, nums):
    	return next(filter(lambda x: nums.count(x) > 1, nums))


    def floydsCycle(self, nums):
    	length = len(nums)
        t = 0
        h = 1
        v = set()
        v.add((t,h))
        while nums[t] != nums[h]:
            t = (t +1) % length
            h = (h+2) % length
            
            if t == h:
                t = (t +1) % length
                h = (h+2) % length
                
            if (t,h) in v:
                t = (t+1) % length
                h = (h+1) % length
                v.add((t,h))
                
        return nums[t]