1class Solution:
2    def reverseWords(self, s: str) -> str:
3        return " ".join(reversed(s.split()))
4