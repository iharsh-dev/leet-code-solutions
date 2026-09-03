1class Solution:
2    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
3        if len(connections) < n - 1:
4            return -1 
5
6        parent = list(range(n))
7
8        def find(x):
9            
10            if parent[x] != x:
11                parent[x] = find(parent[x])
12            
13            return parent[x]
14
15        components = n
16
17        for a,b in connections:
18            ra = find(a)
19            rb = find(b)
20
21            if ra != rb:
22                parent[rb] = ra
23                components -= 1
24        
25        return components - 1
26            
27
28