1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        n = len(nums)
4        i = j = 0
5        curr = 0
6        minn = float('inf')
7        while j < n:
8            curr += nums[j]
9            j+=1               
10            while i < j and curr >= target:
11                minn = min(minn,j - i)
12                curr -= nums[i]
13                i+=1 
14        if minn == float('inf'):
15            return 0
16        
17        return minn