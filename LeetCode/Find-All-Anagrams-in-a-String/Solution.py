1from collections import Counter
2class Solution:
3    def findAnagrams(self, s: str, p: str) -> list[int]:
4        target = Counter(p)
5        n = len(p)
6        curr = Counter(s[:n])
7        ans = []
8        if curr == target:
9            ans.append(0)
10        for i in range(n,len(s)):
11
12            curr[s[i - n]] -= 1
13            curr[s[i]] += 1
14
15            if curr == target:
16                ans.append(i - n + 1)
17        
18        return ans
19
20            
21            
22            