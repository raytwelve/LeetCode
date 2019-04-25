'''
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		i=0
		
		while len(nums2) > 0 and i < m:
			if nums2[0] <= nums1[i]:
				nums1.insert(i, nums2.pop(0))
				nums1.pop()
				m += 1
			i +=1

		while len(nums2) > 0:
			nums1.insert(i, nums2.pop(0))
			nums1.pop()
			i+=1