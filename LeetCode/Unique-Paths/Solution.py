1from functools import cache
2class Solution:
3    def uniquePaths(self, m: int, n: int) -> int:
4        @cache
5        def path(i,j):
6            if i == m - 1 and j == n - 1:
7                return 1
8            a = b = 0
9            if i < m:
10                a = path(i + 1, j)
11            if j < n:
12                b = path( i, j + 1)
13            return a + b
14        return path(0,0)