1from functools import cache
2class Solution:
3    def change(self, amount: int, coins: List[int]) -> int:
4        n = len(coins)
5        coins.sort(reverse = True)
6        @cache
7        def dp(curr, ind):
8            if curr == 0:
9                return 1
10            if curr < 0 or ind == n:
11                return 0 
12            
13            return dp(curr, ind + 1) + dp(curr - coins[ind],ind)
14        return dp(amount,0)