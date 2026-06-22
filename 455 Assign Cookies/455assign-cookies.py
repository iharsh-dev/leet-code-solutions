class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        j = 0
        for i in range(len(s)):
            if j >= len(g):
                break
            if s[i] >= g[j]:
                count+=1
                j+=1
        return count