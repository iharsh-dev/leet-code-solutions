class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s11=list(s1)
        s22=list(s2)
        ans=True
        for i in range(4):
            if s11[i]!=s22[i]:
                if i<2 and s11[i]==s22[i+2]:
                    s22[i],s22[i+2]=s22[i+2],s22[i]
                else:
                    ans=False
                    break
            
        return ans
                    