1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        brack = ['(','{','[']
5        track = [')','}',']']
6        for i in s:
7            if i in brack:
8                stack.append(i)
9            else:
10                if not stack:
11                    return False
12                    
13                m = stack.pop()
14                if brack.index(m) != track.index(i):
15                    return False
16        if not stack:
17            return True
18        
19        return False