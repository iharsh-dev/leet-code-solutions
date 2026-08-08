1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        n = len(matrix)
4        for i in range(n):
5            for j in range(i, n - 1 - i):
6                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
7                matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
8        