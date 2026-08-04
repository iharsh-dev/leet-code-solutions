1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        m = len(needle)
4        n = len(haystack)
5        if m == 0:
6            return 0 
7        
8        for i in range(n-m+1):
9            if haystack[i:i+m] == needle:
10                return i 
11        
12        return -1