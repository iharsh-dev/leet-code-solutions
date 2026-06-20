class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = True
        d = {ch:-1 for ch in s}
        for i in range(len(s)):
            if d[s[i]] == -1:
                d[s[i]] = t[i] 
            else:
                if d[s[i]] != t[i]:
                    check = False
                    break
        b = {ch:-1 for ch in t}
        for i in range(len(s)):
            if b[t[i]] == -1:
                b[t[i]] = s[i] 
            else:
                if b[t[i]] != s[i]:
                    check = False
                    break
        return check