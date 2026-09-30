1class Solution:
2    def maxDepthAfterSplit(self, seq: str) -> list[int]:
3        n = len(seq)
4        ans = [0]*n
5        one = 0
6        two = 0
7        for i in range(n):
8            if seq[i] == '(':
9                ans[i] = one
10                one = 1 if one == 0 else 0
11            else:
12                ans[i] = two
13                two = 1 if two == 0 else 0
14        
15        return ans
16            
17
18