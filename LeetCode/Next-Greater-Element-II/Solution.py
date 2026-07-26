1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        stack = [] 
4        m = len(nums)
5        ans = [-1]*m
6        for i in range(2*m - 1, -1 , -1):
7            ind = i%m
8            while stack and stack[-1] <= nums[ind]:
9                stack.pop()
10            
11            if stack:
12                ans[ind] = stack[-1]
13            
14            stack.append(nums[ind])
15        
16        return ans
17        
18