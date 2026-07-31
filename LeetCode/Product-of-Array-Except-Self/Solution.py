1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        prod = 1 
5        zero = nums.count(0)
6        ans = [0]*n
7        for i in nums:
8            if i != 0:
9                prod*=i 
10        if zero == 1: 
11            for i in range(n):
12                if nums[i] == 0:
13                    ans[i] = prod 
14        elif zero == 0:
15            for i in range(n):
16                ans[i] = prod//nums[i]
17        
18        return ans
19            