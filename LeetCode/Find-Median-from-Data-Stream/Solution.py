1import heapq
2class MedianFinder:
3
4    def __init__(self):
5        self.min_heap = []
6        self.max_heap = []
7
8    def addNum(self, num: int) -> None:
9        a = heapq.heappushpop(self.max_heap,-num)
10        heapq.heappush(self.min_heap,-a)
11        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
12            b = heapq.heappop(self.min_heap)
13            heapq.heappush(self.max_heap,-b)
14
15    def findMedian(self) -> float:
16        if len(self.max_heap) == len(self.min_heap):
17            return (self.min_heap[0] - self.max_heap[0]) / 2
18        
19        return self.min_heap[0]
20
21
22# Your MedianFinder object will be instantiated and called as such:
23# obj = MedianFinder()
24# obj.addNum(num)
25# param_2 = obj.findMedian()