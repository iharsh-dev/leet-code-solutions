class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        mapa = defaultdict(list)
        for i in range(n):
            for j in range(m):
                mapa[i-j].append(mat[i][j])
        for i in mapa.values():
            i.sort()
        for i in range(n):
            for j in range(m):
                mat[i][j]=mapa[i-j][0]
                mapa[i-j].pop(0)
        return mat


            