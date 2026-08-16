1from collections import deque
2import heapq
3class Solution:
4    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
5        que = deque()
6
7        n = len(nums)
8
9        ans = []
10
11        for i in range(n):
12            while que and que[0] <= i - k:
13                que.popleft()
14            
15            while que and nums[que[-1]] <= nums[i]:
16                que.pop()
17            
18            que.append(i)
19
20            if i >= k -1:
21                ans.append(nums[que[0]])
22            
23        return ans
24