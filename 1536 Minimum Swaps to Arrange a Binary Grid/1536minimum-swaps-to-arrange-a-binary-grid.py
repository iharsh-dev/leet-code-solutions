class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        arr=[0]*n
        for i in range(n):
            j=n-1
            count=0
            while j>=0 and grid[i][j]==0:
                count+=1
                j-=1
            arr[i]=count
        num=0
        brr=arr[:]
        brr.sort()
        check=0
        for i in range(n):
            if i > brr[i]:
                check=1
                break
        if check==0:
            for i in range(n):
                for j in range(i,n):
                    if arr[j]>=n-i-1:
                        temp=arr[j]
                        arr.pop(j)
                        arr.insert(i,temp)
                        num+=(j-i)
                        break
        else:
            num=-1
        return num

