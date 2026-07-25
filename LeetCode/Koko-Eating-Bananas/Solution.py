1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        left = 1 
4        right = max(piles) 
5        while left < right:
6            mid = (left + right)//2 
7            hours = 0
8            for i in piles:
9                if i % mid == 0:
10                    hours+=i//mid 
11                else:
12                    hours+=(i//mid + 1)
13            if hours <= h:
14                right = mid 
15            else:
16                left = mid + 1
17        return left