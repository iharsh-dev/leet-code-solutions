1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        
5        arr = [ x*x for x in nums]
6
7        arr.sort(reverse=True)
8
9        pos, neg = 0, 0
10        for i in range((n + 1)//2):
11            pos+=(arr[i])
12        
13        for i in range((n+1)//2,n):
14            neg+=(arr[i])
15        
16        return pos - neg