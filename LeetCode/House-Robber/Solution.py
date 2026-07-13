1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        arr = {}
5        def fun(i):
6            if i >= n:
7                return 0
8            if i not in arr:
9                arr[i] = max(nums[i] + fun(i+2),fun(i+1))
10            return arr[i]
11        return fun(0)