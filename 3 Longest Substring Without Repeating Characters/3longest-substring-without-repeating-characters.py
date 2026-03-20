class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        n=len(s)

        for i in range(n):
            mapa={chr(k):0 for k in range(128) }
            j=i
            count=0
            while j<n:
                if mapa[s[j]]==0:
                    count+=1
                    mapa[s[j]]=1
                else:
                    break
                j+=1
            maxx=max(maxx,count)
        return maxx