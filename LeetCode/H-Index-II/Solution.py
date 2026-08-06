1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        n = len(citations)
4
5        left = 0
6        right = n - 1
7
8        while left <= right:
9            mid = (left + right)//2 
10            if n - mid == citations[mid]:
11                return n - mid 
12            elif n - mid <= citations[mid]:
13                right = mid - 1
14            else:
15                left = mid + 1
16        return n - left
17                
18
19            