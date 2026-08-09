1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m, n = len(matrix), len(matrix[0])
4        row = 0
5        col = n - 1
6        found = True
7        while row < m and col >= 0:
8            if matrix[row][col] == target:
9                return True
10            if matrix[row][col] > target:
11                col -= 1
12            else:
13                row += 1
14        
15        return False