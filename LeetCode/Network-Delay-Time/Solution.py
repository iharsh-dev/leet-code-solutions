1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        INF = float('inf')
4
5        graph = defaultdict(list)
6        for fro , to, fare in times:
7            graph[fro].append((to,fare))
8                
9        time = [INF]*(n+1)
10        time[k] = 0
11        que = deque([(k,0)])
12
13        while que:
14            node, t = que.popleft()
15
16            for i, tt  in graph[node]:
17                if time[i] > t + tt :
18                    time[i] = t + tt
19                    que.append((i, time[i]))
20
21        if max(time[1:]) == INF:
22            return -1
23        
24        return max(time[1:])