1class Solution:
2    def minEatingSpeed(self, piles: list[int], h: int) -> int:
3        left = 1
4        right = max(piles)
5        while left < right:
6            mid = (left+right)//2
7            hours = 0
8            for i in piles:
9                hours += ((i + mid - 1)//mid)
10            
11            if hours <= h:
12                right = mid 
13            else:
14                left = mid + 1
15        
16        return left