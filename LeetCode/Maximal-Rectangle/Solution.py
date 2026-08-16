1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4
5        for i in range(m):
6            for j in range(n):
7                matrix[i][j] = int(matrix[i][j])
8        
9        area = 0
10        for i in range(1,m):
11            for j in range(n):
12                if matrix[i][j] == 1:
13                    matrix[i][j] = matrix[i - 1][j] + 1 
14        for i in range(m):
15            stack1 = []
16            left = [-1] * n
17            stack2 = []
18            right = [n] * n
19            for j in range(n):
20                while stack1 and matrix[i][stack1[-1]] >= matrix[i][j]:
21                    stack1.pop()
22                
23                while stack2 and matrix[i][stack2[-1]] > matrix[i][n - 1 - j]:
24                    stack2.pop()
25                
26                if stack1:
27                    left[j] = stack1[-1]
28                
29                if stack2:
30                    right[n - j - 1] = stack2[-1]
31                
32                stack1.append(j)
33                stack2.append(n - j - 1)
34            for j in range(n):
35                area = max(area,matrix[i][j]*(right[j] - left[j] - 1))
36            
37        return area
38
39
40