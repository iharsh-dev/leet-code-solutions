1class Solution:
2    def reverseWords(self, s: str) -> str:
3        a = list(s.split())
4        return (" ".join(reversed(a))).strip()
5