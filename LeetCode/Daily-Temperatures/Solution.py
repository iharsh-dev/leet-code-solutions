1class Solution:
2    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
3        n = len(temperatures)
4        stack = []
5        ans = [0]*n
6
7        for i in range(n - 1,-1,-1):
8            while stack and temperatures[stack[-1]] <= temperatures[i]:
9                stack.pop()
10            
11            if stack:
12                ans[i] = stack[-1] - i
13            
14            stack.append(i)
15        
16        return ans
17        