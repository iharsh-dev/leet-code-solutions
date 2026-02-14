class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        py = [[0.0]*101 for i in range(101)]
        py[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                if py[i][j]>1:
                    py[i+1][j]+=(py[i][j]-1)/2
                    py[i+1][j+1]+=(py[i][j]-1)/2
                    py[i][j]=1
        return py[query_row][query_glass]
                
