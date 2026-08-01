1from collections import defaultdict
2class Solution:
3    def climbStairs(self, n: int) -> int:
4        memo = defaultdict(int)
5        def dp(step):
6            if step == n:
7                return 1
8            if step > n:
9                return 0
10            if not memo[step]:
11                memo[step] = dp(step+1)+dp(step+2) 
12            return memo[step]
13        return dp(0)
14