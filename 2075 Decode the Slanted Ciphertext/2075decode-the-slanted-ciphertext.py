class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        mat=[['_']*cols for i in range(rows)]
        b = 0
        for i in range(rows):
            for j in range(cols):
                mat[i][j]=encodedText[b]
                b+=1
        mapa = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]!=0:
                    mapa[i-j].append(mat[i][j])
        ans = [item for items in mapa.values() for item in items]
        s = ''.join(ans).rstrip()
        return s