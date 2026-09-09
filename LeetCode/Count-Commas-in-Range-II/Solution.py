1class Solution:
2    def countCommas(self, n: int) -> int:
3        pow = 3
4        comma = 0
5        while 10**pow <= n:
6            if 10**(pow+3) <= n:
7                comma += ((pow//3)*(999*10**pow))
8            else:
9                comma += ((pow//3)*(n - 10**pow + 1))
10            pow+=3
11        
12        return comma