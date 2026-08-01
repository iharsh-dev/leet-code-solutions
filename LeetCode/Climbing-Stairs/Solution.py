1from functools import cache
2class Solution:
3    def climbStairs(self, n: int) -> int:
4        @cache
5        def dp(step):
6            if step == n:
7                return 1
8            if step > n:
9                return 0
10            return dp(step+1)+dp(step+2) 
11        return dp(0)
12