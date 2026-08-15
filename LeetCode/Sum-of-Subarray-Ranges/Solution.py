1class Solution:
2    def subArrayRanges(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        min_left = [-1]*n
6        stack = []
7
8        for i in range(n):
9            while stack and nums[stack[-1]] >= nums[i]:
10                stack.pop()
11            
12            if stack:
13                min_left[i] = stack[-1]
14            
15            stack.append(i)
16        
17        min_right = [n]*n
18        stack = []
19
20        for i in range(n - 1, -1, -1):
21            while stack and nums[stack[-1]] > nums[i]:
22                stack.pop()
23            
24            if stack:
25                min_right[i] = stack[-1]
26            
27            stack.append(i)
28        
29        max_left = [-1]*n
30        stack = []
31
32        for i in range(n):
33            while stack and nums[stack[-1]] <= nums[i]:
34                stack.pop()
35            
36            if stack:
37                max_left[i] = stack[-1]
38            
39            stack.append(i)
40        
41        max_right = [n]*n
42        stack = []
43
44        for i in range(n - 1, -1, -1):
45            while stack and nums[stack[-1]] < nums[i]:
46                stack.pop()
47            
48            if stack:
49                max_right[i] = stack[-1]
50            
51            stack.append(i)
52        
53        ans = 0
54        for i in range(n):
55            ans += ((i - max_left[i])*(max_right[i] - i)*nums[i] - (i - min_left[i])*(min_right[i] - i)*nums[i])
56        
57        return ans
58        