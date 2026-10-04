1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        n, m = len(text1), len(text2)
4
5        dp = [[0]*(m+1) for _ in range(n+1)]
6
7        i, j = 0, 0
8        for i in range(1,n+1):
9            for j in range(1,m+1):
10                if text1[i-1] == text2[j-1]:
11                    dp[i][j] = dp[i-1][j-1] + 1
12                else:
13                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
14        
15        return dp[-1][-1]