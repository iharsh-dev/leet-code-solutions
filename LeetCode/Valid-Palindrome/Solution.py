1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        a = s.lower()
4        b = "".join([char for char in a if char.isalnum()])
5        if b == b[::-1]:
6            return True 
7        
8        return False
9