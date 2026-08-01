1from functools import cache
2class Solution:
3    def minPathSum(self, grid: List[List[int]]) -> int:
4        m = len(grid)
5        n = len(grid[0])
6        @cache
7        def dfs(i,j):
8            a = b = 10**9
9            if i == m - 1 and j == n - 1:
10                return grid[i][j]
11            if i < m - 1:
12                a = dfs(i+1,j)
13            if j < n - 1:
14                b = dfs(i,j+1)
15            return min(a,b) + grid[i][j]
16        return dfs(0,0)
17
18
19