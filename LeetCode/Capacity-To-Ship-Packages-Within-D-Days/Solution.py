1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        left = max(weights)
4        right = sum(weights)
5        while left < right:
6            mid = (left + right)//2
7            summ = 0
8            day = 1
9            for weight in weights:
10                if summ + weight> mid:
11                    day+=1
12                    summ = 0
13                summ+=weight
14            if day <= days:
15                right = mid 
16            else:
17                left = mid + 1 
18        return left