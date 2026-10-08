1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        stack = 0
4        ans = []
5        for i in s:
6            if i == '(':
7                if stack != 0:
8                    ans.append(i)
9                stack += 1
10            else:
11                stack -= 1
12                if stack != 0:
13                    ans.append(i)
14            
15        return "".join(ans)
16            