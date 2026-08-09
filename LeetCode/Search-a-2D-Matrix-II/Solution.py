1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m, n = len(matrix), len(matrix[0])
4        row = 0
5        col = n - 1
6        while row < m and col >= 0:
7            if matrix[row][col] == target:
8                return True
9            if matrix[row][col] > target:
10                col -= 1
11            else:
12                row += 1
13        
14        return False