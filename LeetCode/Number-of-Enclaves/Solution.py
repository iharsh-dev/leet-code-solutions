1class Solution:
2    def numEnclaves(self, grid: List[List[int]]) -> int:
3        n, m = len(grid), len(grid[0])
4        
5        queue = deque()
6
7        direction = [(0,1),(1,0),(0,-1),(-1,0)]
8
9        for j in range(n):
10            if grid[j][0] == 1:
11                grid[j][0] = -1
12                queue.append((j,0))
13            if grid[j][m-1] == 1:
14                grid[j][m-1] = -1
15                queue.append((j,m-1))
16        
17        for j in range(m):
18            if grid[0][j] == 1:
19                grid[0][j] = -1
20                queue.append((0,j))
21            if grid[n-1][j] == 1:
22                grid[n-1][j] = -1
23                queue.append((n-1,j))
24        
25        while queue:
26            i, j = queue.popleft()
27            for x, y in direction:
28                if 0 <= x + i < n and 0 <= y + j < m and grid[x+i][y+j] == 1:
29                    grid[x+i][y+j] = -1 
30                    queue.append((x+i,y+j))
31        
32        count = 0
33        for i in range(n):
34            for j in range(m):
35                if grid[i][j] == 1:
36                    count+=1
37                
38        return count