class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        check=0
        ans=False
        for i in range(n):
            found=False
            for j in range(n):
                if target[i][j]!=mat[i][j]:
                    check+=1
                    found=True
                    break
            if found:
                break
        for i in range(n):
            found=False
            for j in range(n):
                if target[i][j]!=mat[n-j-1][i]:
                    check+=1
                    found=True
                    break
            if found:
                break
            
        for i in range(n):
            found=False
            for j in range(n):
                if target[i][j]!=mat[n-i-1][n-j-1]:
                    check+=1
                    found=True
                    break
            if found:
                break

        for i in range(n):
            found=False
            for j in range(n): 
                if target[i][j]!=mat[j][n-i-1]:
                    check+=1
                    found=True
                    break
            if found:
                break
        if check<4:
            ans=True
        return ans