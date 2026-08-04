1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        n = len(bloomDay)
4
5        if m*k > n:
6            return -1 
7        
8        left = min(bloomDay)
9        right = max(bloomDay)
10
11        while left < right:
12            mid = (left + right)//2
13            ans = 0
14            i = 0
15            while i < n:
16                count= 0
17                while i < n and bloomDay[i] <= mid:
18                    count+=1 
19                    i+=1
20                i+=1
21                ans+=(count//k)
22            if ans < m:
23                left = mid + 1
24            else:
25                right = mid
26
27        return right
28
29                
30        
31        