class Solution:
    def maxDepth(self, s: str) -> int:
        arr = 0
        maxx = 0
        for i in s:
            if i == '(':
                arr+=1 
            elif i == ')':
                maxx = max(maxx,arr)
                arr-=1 
        return maxx