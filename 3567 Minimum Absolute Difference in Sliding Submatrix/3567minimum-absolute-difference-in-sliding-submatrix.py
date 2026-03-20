class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        ans=[[0]*(n-k+1) for i in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                a=[]
                for l in range(k):
                    a+=grid[i+l][j:j+k]
                a.sort()
                minn=float('inf')
                for x in range(k*k-1):
                    if a[x]!=a[x+1]:
                        minn=min(minn,a[x+1]-a[x])
                if minn==float('inf'):
                    minn=0
                ans[i][j]=minn
        return ans