class Solution:
    def numSteps(self, s: str) -> int:
        a = [int(b) for b in s]
        count=0
        while True:
            if len(a)==1 and a[0]==1:
                break
            elif a[-1]==1:
                count+=1
                for i in range(len(a)-1,-1,-1):
                    if a[i]==0:
                        a[i]=1
                        break
                    if a[i]==1:
                        a[i]=0
                if a[0]==0:
                    a.insert(0,1)
            else:
                count+=1
                a.pop()
        return count
                    


