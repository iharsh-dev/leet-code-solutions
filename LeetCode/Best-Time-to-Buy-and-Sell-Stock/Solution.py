1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        stack = []
6        best = [0]*n
7        best[-1] = prices[-1]
8
9        for i in range(n-2,-1,-1):
10            best[i] = max(best[i+1],prices[i])
11        
12        profit = 0
13        for i in range(n):
14            profit = max(profit,best[i] - prices[i])
15        
16        return profit