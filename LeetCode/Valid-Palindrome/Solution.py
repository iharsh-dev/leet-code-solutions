1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        a = []
4        for i in s:
5            o = ord(i)
6            if 65 <= o <= 90:
7                a.append(chr(o + 32))
8            elif 97 <= o <= 122 or 48 <= o <= 57:
9                a.append(i)
10        if a == a[::-1]:
11            return True
12        else:
13            return False
14