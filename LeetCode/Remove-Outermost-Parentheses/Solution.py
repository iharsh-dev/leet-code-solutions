1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        arr = 0
4        brr = []
5        j = 0 
6        for i in range(len(s)):
7            if s[i] == '(':
8                arr+=1 
9            else:
10                arr-=1
11            if arr == 0:
12                brr.append(s[j:i+1])
13                j = i + 1 
14        for i in range(len(brr)):
15            brr[i] = brr[i][1:-1] 
16        ans = ""
17        for i in brr:
18            ans+=i 
19        return ans