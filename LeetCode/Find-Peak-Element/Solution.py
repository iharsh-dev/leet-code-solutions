1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        if n == 1:
6            return 0
7
8        if nums[0] > nums[1]:
9            return 0
10        
11        if nums[-1] > nums[-2]:
12            return n-1
13        
14        for i in range(1,n-1):
15            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
16                return i
17