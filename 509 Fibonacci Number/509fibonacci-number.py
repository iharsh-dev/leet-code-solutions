class Solution:
    def fib(self, n: int,memo={}) -> int:
        if memo==None:
            memo={}
        if n<=1:
            return n
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n] = self.fib(n-1,memo)+self.fib(n-2,memo)
                return memo[n]