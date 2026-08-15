1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        if sum(nums) == 0:
4            return 0
5        
6        n = len(nums)
7        bit = 0
8
9        for i in range(n):
10            bit = bit^nums[i]
11        
12        return n if bit!=0 else n - 1