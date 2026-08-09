1from collections import Counter
2class Solution:
3    def isAnagram(self, s: str, t: str) -> bool:
4        if Counter(s) == Counter(t):
5            return True
6        
7        return False