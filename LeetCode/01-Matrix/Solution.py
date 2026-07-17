1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        n = len(mat)
4        m = len(mat[0])
5        ans = [[10**9+1]*m for _ in range(n)]
6        queue = []
7        for i in range(n):
8            for j in range(m):
9                if mat[i][j] == 0:
10                    queue.append((i,j))
11                    ans[i][j] = 0 
12        for i,j in queue:
13            if i > 0:
14                if ans[i-1][j] == 10**9+1:
15                    ans[i-1][j] = ans[i][j]+1 
16                    queue.append((i-1,j))
17            if i < n - 1:
18                if ans[i+1][j] == 10**9+1:
19                    ans[i+1][j] = ans[i][j]+1 
20                    queue.append((i+1,j))
21            if j > 0:
22                if ans[i][j-1] == 10**9+1:
23                    ans[i][j-1] = ans[i][j]+1 
24                    queue.append((i,j-1))
25            if j < m - 1:
26                if ans[i][j+1] == 10**9+1:
27                    ans[i][j+1] = ans[i][j]+1 
28                    queue.append((i,j+1))
29        return ans