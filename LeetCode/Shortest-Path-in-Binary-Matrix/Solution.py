1from collections import deque
2class Solution:
3    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
4        n = len(grid)
5        
6        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
7            return -1
8        
9        INF = float('inf')
10
11        dist = [[INF]*n for _ in range(n)]
12        dist[0][0] = 0
13
14        que = deque([(0,0,0)])
15        x_d = [0,1,-1,0,1,-1,1,-1]
16        y_d = [1,0,0,-1,1,-1,-1,1]
17
18        while que:
19            dis, x, y = que.popleft()
20            for i, j in zip(x_d,y_d):
21                if 0 <= x + i < n and 0 <= y + j < n and grid[x+i][y+j] == 0:
22                    if dis + 1 < dist[x+i][y+j]:
23                        dist[x+i][y+j] = dis + 1
24                        que.append((dis + 1, x + i, y + j))
25        ans = dist[n-1][n-1] + 1
26        return ans if ans!= INF else -1
27                    
28