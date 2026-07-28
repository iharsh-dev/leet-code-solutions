1class Solution:
2    def numberOfSubstrings(self, s: str) -> int:
3        n = len(s)
4        freq = {'a':0, 'b':0, 'c':0}
5        left = 0
6        right = 0
7        count = 0
8        while right < n:
9            freq[s[right]]+=1
10            while freq['a'] and freq['b'] and freq['c']:
11                count+=(n - right)
12                freq[s[left]]-=1
13                left+=1
14            right+=1
15        return count