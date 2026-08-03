1from collections import deque, Counter
2import heapq
3class Solution:
4    def leastInterval(self, tasks: List[str], n: int) -> int:
5        freq = Counter(tasks)
6        que = deque()
7        heap = []
8        for key in freq:
9            heap.append(-freq[key])
10        heapq.heapify(heap)
11        time = 0
12        while heap or que:
13            time+=1 
14            if heap:
15                node = 1 + heapq.heappop(heap)
16                if node!= 0:
17                    que.append((node,time + n))
18            if que:
19                if que[0][1] == time:
20                    nod , tim = que.popleft()
21                    heapq.heappush(heap,nod)
22        return time
23
24            
25