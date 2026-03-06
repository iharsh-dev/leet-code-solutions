class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n=len(s)
        ans=True
        for i in range(n-1):
            if s[i]=='0' and s[i+1]=='1':
                ans=False
        return ans
        
            
        