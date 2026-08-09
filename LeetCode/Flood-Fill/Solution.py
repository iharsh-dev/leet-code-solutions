1from collections import deque
2class Solution:
3    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
4        n = len(image)
5        m = len(image[0])
6
7        direction = [(0,1),(1,0),(0,-1),(-1,0)]
8
9        org = image[sr][sc]
10        if org == color:
11            return image
12        
13        image[sr][sc] = color
14        queue = deque()
15        queue.append((sr,sc))
16
17        while queue:
18            i, j = queue.popleft()
19
20            for x, y in direction:
21                if 0 <= i + x < n and 0 <= j + y < m and image[i + x][j + y] == org:
22                    queue.append(( i + x,j + y))
23                    image[x + i][j + y] = color
24        return image