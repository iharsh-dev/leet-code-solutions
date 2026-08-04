1class Solution:
2    def findKthPositive(self, arr: List[int], k: int) -> int:
3        m = 0
4        for i in range(1,max(arr)):
5            if i not in arr:
6                m+=1 
7            if m == k:
8                return i
9        return max(arr) + k - m