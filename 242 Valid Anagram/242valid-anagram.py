class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        else:
            count = [0]*26 

            for ch in range(len(s)):
                count[ord(s[ch])-ord('a')]+=1 
                count[ord(t[ch])- ord('a')]-=1 
            return all(x==0 for x in count)
