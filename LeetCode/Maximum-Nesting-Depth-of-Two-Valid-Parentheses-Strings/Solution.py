1class Solution:
2    def maxDepthAfterSplit(self, seq: str) -> list[int]:
3        n = len(seq)
4        ans = [0]*n
5        one = 0
6        two = 0
7        for i in range(n):
8            if seq[i] == '(':
9                if one % 2 == 0:
10                    ans[i] = 0
11                else:
12                    ans[i] = 1
13                one += 1
14            else:
15                if two % 2 == 0:
16                    ans[i] = 0
17                else:
18                    ans[i] = 1
19                two += 1
20        
21        return ans
22            
23
24