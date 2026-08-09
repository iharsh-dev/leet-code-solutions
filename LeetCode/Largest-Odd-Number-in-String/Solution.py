1class Solution:
2    def largestOddNumber(self, num: str) -> str:
3        i = len(num) - 1
4        while i >= 0:
5            if int(num[i]) % 2 != 0:
6                break
7            i-=1 
8        return num[:i+1]