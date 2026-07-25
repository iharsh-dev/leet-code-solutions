1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        i = 0
4        j = len(nums) - 1 
5        while i < j:
6            mid = (i+j)//2 
7            if nums[mid] > nums[mid+1]:
8                j = mid 
9            else:
10                i = mid + 1 
11        return i 
12            