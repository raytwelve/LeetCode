'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

# Python
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		i = 0
		while i < len(nums)-1:
			if nums[i] == nums[i+1]:
				nums.pop(i+1)
			else:
				i += 1


# Java
class Solution {
    public int removeDuplicates(int[] nums) {
        int l=1;
        for(int i = 0; i<nums.length-1; i++) {
            if (nums[i] != nums[i+1]) {
                nums[l] = nums[i+1];
                l++;
            }
        }
        return l;
    }
}