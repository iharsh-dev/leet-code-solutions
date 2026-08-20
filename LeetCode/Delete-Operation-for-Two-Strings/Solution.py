1from functools import cache
2class Solution:
3    def minDistance(self, word1: str, word2: str) -> int:
4        @cache
5        def dp(i,j):
6            if i == len(word1):
7                return len(word2) - j
8            
9            if j == len(word2):
10                return len(word1) - i
11            
12            if word1[i] == word2[j]:
13                return dp(i+1,j+1)
14            
15            return 1 + min(dp(i + 1, j),dp(i, j + 1))
16        
17        return dp(0,0)