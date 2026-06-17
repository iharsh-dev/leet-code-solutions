class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = 0
        brr = []
        j = 0 
        for i in range(len(s)):
            if s[i] == '(':
                arr+=1 
            else:
                arr-=1
            if arr == 0:
                brr.append(s[j:i+1])
                j = i + 1 
        for i in range(len(brr)):
            brr[i] = brr[i][1:-1] 
        ans = ""
        for i in brr:
            ans+=i 
        return ans