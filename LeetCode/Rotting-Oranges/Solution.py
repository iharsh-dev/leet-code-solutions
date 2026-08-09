1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        m, n = len(grid), len(grid[0])
5
6        queue = deque()
7        direction = [(0,1),(1,0),(0,-1),(-1,0)]
8        time = 0
9        fresh = 0
10
11        for i in range(m):
12            for j in range(n):
13                if grid[i][j] == 2:
14                    queue.append((i,j))
15                if grid[i][j] == 1:
16                    fresh+=1
17        while True:
18            arr = deque()
19            if fresh == 0 or len(queue) == 0:
20                break
21            while queue:
22                row, col = queue.popleft()
23
24                for i, j in direction:
25                    if 0 <= row + i < m and 0<= col + j < n and grid[row + i][col + j] == 1:
26                        grid[row + i][col + j] = 2
27                        arr.append((row + i,col + j))
28                        fresh -=1
29            queue = arr
30            time += 1
31            
32        if fresh:
33            return -1 
34        
35        return time
36            
37                        
38