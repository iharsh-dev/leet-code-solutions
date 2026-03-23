class Solution:
    def climbStairs(self, n: int , memo={}) -> int:
        if memo is None:
            memo={}
        if n==0 or n==1:
            return 1
        elif n>=2:
            if n in memo:
                return memo[n]
            else:
                memo[n]= self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
                return memo[n]
        