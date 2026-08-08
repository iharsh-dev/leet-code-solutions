1from functools import cache
2class Solution:
3    def maxProduct(self, nums: List[int]) -> int:
4        n = len(nums)
5        minn = maxx = res  = nums[0]
6
7        for i in range(1,n):
8            x = nums[i]
9
10            new_max = max(x,x*maxx,x*minn)
11            new_min = min(x,x*minn,x*maxx)
12
13            maxx = new_max 
14            minn = new_min 
15
16            res = max(res , maxx)
17        
18        return res