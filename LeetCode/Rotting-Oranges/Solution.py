1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        m = len(grid[0])
5        queue = []
6        for i in range(n):
7            for j in range(m):
8                if grid[i][j] == 2:
9                    queue.append((i,j))
10        time = 0
11        while True:
12            arr = []
13            for i,j in queue:
14                if i > 0:
15                    if grid[i-1][j] == 1:
16                        arr.append((i-1,j))
17                        grid[i-1][j] = 2
18                if i < n-1:
19                    if grid[i+1][j] == 1:
20                        arr.append((i+1,j))
21                        grid[i+1][j] = 2
22                if j > 0:
23                    if grid[i][j-1] == 1:
24                        arr.append((i,j-1))
25                        grid[i][j-1] = 2
26                if j < m-1:
27                    if grid[i][j + 1] == 1:
28                        arr.append((i,j+1))
29                        grid[i][j+1] = 2 
30            if len(arr) == 0:
31                break 
32            queue = arr[:]
33            time+=1
34        count = 0 
35        for i in grid:
36            count += i.count(1)
37        if not count:
38            return time 
39        else:
40            return -1
41