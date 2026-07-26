1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack = []
4        ans = {}
5        for i in reversed(nums2):
6            while stack and stack[-1] < i:
7                stack.pop()
8            
9            if stack:
10                ans[i] = stack[-1]
11            else:
12                ans[i] = -1
13            
14            stack.append(i)
15        
16        return [ans[i] for i in nums1]