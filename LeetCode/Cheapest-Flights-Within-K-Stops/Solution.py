1from collections import deque,defaultdict
2class Solution:
3    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
4        INF = float('inf')
5
6        graph = defaultdict(list)
7        for fro , to, fare in flights:
8            graph[fro].append((to,fare))
9                
10        cost = [INF]*n
11        cost[src] = 0
12        que = deque([(0,src,0)])
13
14        while que:
15            stop, node, money = que.popleft()
16
17            if stop > k :
18                break
19
20            for i, fare in graph[node]:
21                if cost[i] > money + fare:
22                    cost[i] = money + fare 
23                    que.append((stop + 1, i, cost[i]))
24        
25        if cost[dst] == INF:
26            return -1 
27        
28        return cost[dst]
29            
30        