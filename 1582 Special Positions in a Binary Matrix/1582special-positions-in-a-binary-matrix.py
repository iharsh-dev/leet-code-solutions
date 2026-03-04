class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        count=0
        for i in range(m):
            if sum(mat[i])==1:
                b=mat[i].index(1)
                num=0
                for j in range(m):
                    num+=mat[j][b]
                if num==1:
                    count+=1
        return count